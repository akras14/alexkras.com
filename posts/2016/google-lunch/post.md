Two weeks ago I wrote a blog post with a controversial title [Google may be stealing your mobile traffic](https://www.alexkras.com/google-may-be-stealing-your-mobile-traffic/), where I outlined some criticism of [Accelerated Mobile Pages](https://www.ampproject.org/) (AMP) project. Shortly after Paul Bakaus (a developer advocate for AMP project) invited me to join him and Malte Ubl (product manager for AMP project) for lunch to further discuss my concerns.

My original post was a bit confusing and should have been 2 separate posts. 90% was simply me outlining mistakes that I've made implementing AMP on my site. The other 10% I believe to be a valid criticism of the AMP project.

## The Concerns

There were 2 main concerns that I brought up about the AMP implementation:

1. Google was caching AMP pages and serving cached version from their search results.
1. Google provided a tool bar at the top, with a link to the original source, but there was no easy way to copy or click through to that link. This UX was encouraging users to get back to Google search results instead.

<img src="https://www.alexkras.com/wp-content/uploads/3-close-button.png" alt="3-close-button" width="563" height="522" />

## Web Cache

The web caching aspect of AMP is clearly documented, but it was something that I completely overlooked.  

When I first heard of AMP I thought of it as a sub-set of HTML with a JavaScript library that will allow to speed up the mobile web.

Turns out the AMP vision also included a web cache that would allow content providers (Google, Bing, Pinterest, LinkedIn etc) to serve the content much faster.

### Can the cache be optional?

My first question was if I could get the speed up that AMP provides without participating in the cache aspect. The answer was yes and no.

**Yes**. The AMP project is open source and there is nothing stopping anyone from including it in their pages. The only way Google will know to cache the APM page is when non AMP page has a `rel="amphtml"` link on it, pointing to the AMP version. i.e.

`<link rel="amphtml" href="https://www.example.com/url/to/amp/document.html">`

Removing this link will essentially "disable" the AMP cache.

Another option is to remove the `amp` tag from the `html` tag inside of the AMP page.

```
<html amp lang="en">
...
</html>
```
to 
```
<html>
...
</html>
```

HTML pages are not valid AMP pages without the `amp` tag. Therefore removing this tag will prevent the page from being cached.

**No**. While you'll get the optimized page loading that AMP provides, without caching you will not get:

- AMP icon in Google search.
- Chance to appear in AMP specific features such as Top Stories Carousel.
- Content providers (i.e. Google) will not be able to pre-fetch your content. Meaning a delay (comparing to other AMP sites) from when user clicks on your link to when your content is presented in front of them.

**Bottom line: The web cache is the core aspect of AMP project and the benefits of using AMP without cache are greatly reduced.**

*Relevant side note: From what I was told, currently the AMP library does not play nice with some other (don't know the specifics) JavaScript libraries. Make sure to test your use case carefully.*

## Fixing the link

Even though the web cache sounds a bit scary, I can definitely see the benefit that it provides. I probably would have never made such a big deal about the way AMP was working, has the "get the original link" experience been half decent.

At the very least I want to easily:

1. Click through to the original article ( not hosted on Google, probably not the AMP version).
1. Copy the link to the original article, so I can share it through any internet connected device.

I think I did a decent job communicating this concern to Paul and Malte. They both assured me that they understood the problem and are confident that they can find a solution that will work for everyone.

That being said, I am not sure if "fixing" the link is their top priority. Personally, I will not feel 100% comfortable with AMP until this issue is resolved.

In my mind **the URL is the cornerstone of the web** and it must be cherished and protected.

## WordPress Integration

A lot of my pain with AMP came not from the AMP project itself, but rather from miss-understanding how AMP plugin for WordPress worked. It acted like a new theme that stripped out almost everything except for the post content from my original theme, removing such things as analytics and comments. 

While I noticed comments being removed, I did not realize it applied to analytics and other scripts. I've also made a false assumption that users will have an easy way to get to the "original" version of my post, where they will be able to access all of the removed content.

As a result of my original post, some [Github issues](https://www.alexkras.com/google-may-be-stealing-your-mobile-traffic/#comment-55326) were created for WordPress AMP plugin, therefore things might get better in the future.

I did bring up the current state of the WordPress AMP plugin and Malte mentioned that WordPress was a partner in the AMP project. I am not sure exactly what "partner" means in this case.

What was interesting is that Google worked very closely with major publishers, such as BBC and Daily Mail, to make sure that they were happy with the AMP experience. My guess is that the Google team and the WordPress team did not work as closely on the AMP integration, even though Paul and Malte are aware of a number of issues with the WordPress plugin. 

As AMP was gaining steam, more and more small time WordPress publishers (such as myself) enabled AMP support and began participating in the AMP ecosystem. As WordPress AMP pages began showing up in Google search results, a number of confused and upset users (like myself two weeks ago) began to grow, making Google look more evil then they might have actually been.

I think the big difference here is that the big brands are much less concerned about click through rates to their original content. As long as their analytics and ads work, and their server loads are reduced, they are happy. They know that visitors will remember if they read something on BBC, even if the URL showed up as `google.com/something`. Little guys like myself don't have this luxury.

While WordPress integration is not Google's responsibility, I think fixing it is very important for the success of the AMP project.

## Fat bar at the top

I didn't get to bring up one more concern expressed in my original article. Google presents a thick bar at the top of the AMP view, that has the close (x) button and the (view only) URL of the original source. The bar remains at the top and takes up roughly 10-15% of overall screen.

I did not bring this up because I forgot :). I can also see it as part of a solution to the link issue. For example the URL can become clickable/copy-able or the bar can contain a button to allow copying the original URL.

I've followed up with Malte via email and he let me know that the bar only stays fixed to the top in mobile browsers, not in the Google native app. Additionally, in Chrome browser it will scroll out of the view as you scroll into content. The same behavior will land in mobile Safari soon, but they are still working out some bugs.

## Conclusion

I don't think that Google set out to steal our traffic. In Malte's own words, from the start Google has been very careful to construct a project in such a way that publishers maintain full control of their content. Stealing content, is exact opposite of what they are trying to achieve.

At the same time, it is clear to me that AMP is not as decentralized as the original web.

When I first learned of AMP I assumed it to be a smaller and optimized subset of existing Web. As I learned more about the project, I realized that it was it's own thing. AMP acts as a new layer created on top of the existing web. It functions similarly, but at the same time creates a number of different paradigms.

I **am** keeping my WordPress AMP plugin turned on. Even given all of the concerns with the AMP project and the WordPress AMP plugin, AMP gets one thing right - **loads content really fast on mobile devices**. For that, a lot of little things can be (temporarily) forgotten.

At the same time I hope that people who chose to participate in the AMP ecosystem will understand all of the trade-offs involved and get to make an informed decision.

I would also like to remind that the link concerned can be addressed short term by optimizing AMP view below the fat bar (just like some of the big publishers are doing now). 

Here is the list of optimization suggestions from my initial post:

1. Make sure your Analytics tracking code is properly installed.
1. Make sure you have a header that points back to your main site.
1. If your site has a menu, make sure it is visible in the AMP version.
1. Make the title of the post clickable, taking the user back to non AMP version of the page.
1. Make sure your ads and other promotional material is properly integrate into the AMP version.

Last but not least, I would like to say that the AMP project appears to be in good hands. Both Paul and Malte are very open to constructive criticism and discussing how AMP project can be improved. So much so, that they are willing to take their time to have a lunch with some random guy from the internet. 

While their lunch capacity is probably limited, if you have any feedback on the AMP project please make sure to let them know via [GitHub Issues](https://github.com/ampproject/amphtml/issues/new), Stack Overflow, or the AMP mailing list. Updated list of all those links can be found under the [Support section of the AMP site](https://www.ampproject.org/support/faqs/).
