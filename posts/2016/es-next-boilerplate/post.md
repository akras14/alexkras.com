**TLDR; [Visit this repo for minimum ES6+ Boilerplate](https://github.com/akras14/es-next-boilerplate)**

Lately a lot people have been writing about how much they miss the good old days of JavaScript development. Five years ago creating a new web project looked as follows:

1. Create an `index.html` file.
2. Create a JavaScript file.
3. Require your JavaScript file in your `index.html` file.
4. Open your `index.html` file in your favorite browser of choice.

Today, starting a project might look more like:

1. Install or update Node.
2. Install or update NPM.
3. Install Babel and any other build tools that you use.
4. Copy over your old configs for all of the build tools.
5. Realize that some of the build tools have breaking changes since you've last used them.
6. Decide that you want to understand latest and greatest vs. using the old version.
7. Spend few hours reading various docs on how to get all your build tools to work.
8. Create an `index.html` file.
9. Require your transpiled JavaScript file in your `index.html` file.
10. Open your `index.html` file in your favorite browser of choice.

Sure, you could still do it the old way, but then you will be missing out on all the good stuff that has happened in the JavaScript community in the past 5 year. On the flip side, setting all of this up takes so much activation energy that sometimes I find myself giving up on the project before writing a single line of code.

## Finding a better way

I've create [this repo](https://github.com/akras14/es-next-boilerplate) which I intend to keep "dead simple". No bells and wistles. I want the experience to be as close as possible to the way it used to be 5 years ago, while at the same time giving me the needed pieces of the modern stack.

The master project is the minimum set up needed to run Babel that would transpile ES6 to ES5.

Since it's runs with NPM Scripts, in theory it should not have any external dependencies. All that is needed is:

1. Clone and rename the repo (and may be remove the .git folder).
1. run `npm install`
1. In one terminal tab run `npm run watch`
1. In another terminal tab run `npm start`
1. Open your browser to `http://127.0.0.1:8080`

## But I want more

So do I. Right of the bet I wanted to at least have `eslint` support. Instead of hooking it into the main (master) branch, I've create a new recipe branch called [eslint](https://github.com/akras14/es-next-boilerplate/tree/eslint). That way I can clone the needed branch, and go from there.

## Whats next

I plan to add more recipes to the repo as I go along. Next candidate, for example, is adding support for React.

Since, I know a lot of people are suffering from a similar problem, I wanted to open this up to the public. Please let me know if you thing something can be improved or suggest a new recipe.

