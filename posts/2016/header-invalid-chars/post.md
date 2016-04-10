A few weeks ago our production code started to throw a weird error, that looked like this:

```
_http_outgoing.js:351
      throw new TypeError('The header content contains invalid characters');
      ^

TypeError: The header content contains invalid characters
    at ServerResponse.OutgoingMessage.setHeader (_http_outgoing.js:351:13)
```

This was very strange, since it was coming from a code that used to work for a long time. The only thing that has changed was the Node version.

I've tried Googling for the issue, but all I could find was references to a bunch of various [GitHub issues](https://github.com/search?q=The+header+content+contains+invalid+characters&type=Issues&utf8=%E2%9C%93) from all kinds of projects.

After some research, I was able to narrow down the error to the Node update for version [4.3.0](https://github.com/nodejs/node/commit/58db386a1be17499a444df6a78743c9dfb3cf) via [this commit](https://github.com/nodejs/node/commit/7bef1b790727430cb82bf8be80cfe058480de100).

## Why

The update was done for security reasons and to better comply with http spec. You can read more about the underlying security issues [in the commit itself](https://github.com/nodejs/node/commit/58db386a1be17499a444df6a78743c9dfb3cf). 

You can read more about the actual spec in this [Stack Overflow Question](http://stackoverflow.com/questions/19028068/illegal-characters-in-http-headers), which also provides relevant links to the actual HTTP 1.1 spec ([section 2.2](http://www.w3.org/Protocols/rfc2616/rfc2616-sec2.html#sec2.2) and [section 4.2](http://www.w3.org/Protocols/rfc2616/rfc2616-sec4.html#sec4.2)).

TLDR; version is as follows:

1. Each header looks something like this: `Accept-Encoding: gzip,deflate`
2. `Accept-Encoding` - is the header **name**
3. `gzip,deflate` - is the header **value**
4. Only some characters are allowed in the header value (mostly English ASCII)
5. Even less characters are allows in the header name

An unwanted consequence of this update is that various node projects (that did not follow the spec, but that used to work just fine) all of the sudden broke.

## What to do about it

There could be 2 reasons for you to see this error: 

1. One of your project's dependencies was sending headers that did not comply with the spec
2. Your own code did not comply with the spec

### Case 1

If one of your project's dependencies did not comply with the spec, chances are they already have a fix in place.

Simply update to the latest version and it should solve the problem.

If the dependency does not have a fix yet, all you can do is file an issue and hope that they will resolve it soon.

### Case 2

If you own code did not follow the spec, you'll have to look at your specific implementation.

In many cases the issue can be **remedied short term**, by removing invalid characters from your headers. The **long term fix**, should involve re-engineering your app to never send invalid headers in the first place.

I've created [this repo](https://github.com/akras14/validate-http-headers) to demo an appraoch that can be taken for a short term fix.

## Overview of the Demo repo

The demo repo has 2 important files:
- [rules.js](https://github.com/akras14/validate-http-header/blob/master/rules.js)
- [example.js](https://github.com/akras14/validate-http-header/blob/master/index.js)

### rules.js



If you look at the [rules.js](https://github.com/akras14/validate-http-header/blob/master/rules.js) file you will see that it exports 4 functions:

- For the header name
    - **validHeaderName** - Accepts a header name and returns true if header name is valid
    - **cleanHeaderName** - Accepts a header name and returns a valid header name, removing unwanted characters
- For the header value
    - **validHeaderValue** - Accepts a header value and returns true if header value is valid
    - **cleanHeaderValue** - Accepts a header value and returns a valid header value, removing unwanted characters

The two **validate** functions validHeaderName and validHeaderValue are using copy/pasted `checkInvalidHeaderChar` and `checkIsHttpToken` from [the node source](https://github.com/nodejs/node/blob/master/lib/_http_common.js).

**These functions will need to be updated as the Node implementation changes.**

The **clean** functions used the same logic as the **validate** functions, but instead of simply returning true or false, they return a new header name or value with unwanted characters removed.

It may be helpful to look at the [test file for rules.js](https://github.com/akras14/validate-http-header/blob/master/test/rules.test.js) too see some examples of valid and invalid headers.

### example.js

In [example.js](https://github.com/akras14/validate-http-header/blob/master/example.js) you can see a sample implementation of how you might want to hook something like rules.js into your own code.

It's a module that exports only one function called **cleanHeaders**, which accepts http headers represented as a JavaScript object, and goes through every header name(key) and value, removing unwanted characters.

You can check out the [test file for example.js](https://github.com/akras14/validate-http-header/blob/master/test/example.test.js) to see how it works. But it will boil down to something like this:

```
var clean = require("../example");
var someHeaders = {
  "some(name": "жsome value",
  "some other name": "some other valueж"
};

var cleanHeaders = clean(someHeaders);
```

If you use the `cleanHeaders` in your application, the error should go away.

*Note: You may notice that [example.js](https://github.com/akras14/validate-http-header/blob/master/example.js) does two passes through, once simply checking if header is valid, and one more time to remove unwanted characters. I personally prefer that approach because I didn't want to mess with headers that did not need to be messed with. But you can just run it through the cleanHeaderName and cleanHeaderValue right away, to gain faster performance.*

## Conclusion

I thought about releasing this module as an npm package, but for now decided against it, mainly to avoid the [left-pad](http://blog.npmjs.org/post/141577284765/kik-left-pad-and-npm) type of situation. If you WOULD like to have it released as an NPM module, please let me know in the comments or on GitHub.

I hope this post was helpful, but please take everything with a [grain of salt](https://github.com/akras14/validate-http-headers/blob/master/LICENSE).
