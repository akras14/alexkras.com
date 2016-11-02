Two weeks ago I wrote a blog post with a controversial title [Google may be stealing your mobile traffic](https://www.alexkras.com/google-may-be-stealing-your-mobile-traffic/) where I outlined some criticism of [Accelerated Mobile Pages(AMP)](https://www.ampproject.org/) project. Shortly after, Paul Bakaus (a developer advocate for AMP project reached) invited me to join him and Malte Ubl (product manager for AMP project) for lunch, to further discuss my concerns.

My original post wost a bit confusing and should have been 2 separate posts. 90% was simply me outlining mistakes that I've made implementing AMP on my site, and has nothing to do with Google. The other 10%, however, I believe to be a valid criticism of the AMP project.

## The Concerns

There were 2 main concerns that I've had with the AMP implementation:

1. Google was caching AMP pages and serving cached version from their search results
1. Google provided a tool bar at the top, with a link to the original source, but there was no easy way to copy or click through to that source. This UX was encouraging the user to get back to Google search results.

## Web Cache

The web caching aspect of AMP is clearly documented, but it was something that I overlooked completely.  

When I first heard of AMP I thought of it as a sub-set of HTML that will allow to speed up the web, with some JavaScript libraries to help facilitate that.

Turns out that the AMP vision also included a web cache that would allow to serve the content much faster. As was explained to me, this cache is not only used by Google but by other content providers such as Bing, LinkedIn and Pinterest.

### Can the cache be optional?

My first question was, if I could just opt out of cache to get other AMP benefits. The answer is yes and no.

Yes. The AMP project is open source, and there is nothing stopping anyone from including it in their pages. The only way Google will not to cache the APM page if you specify a link on non-AMP page to point to the optimized version. i.e.

`<link rel="amphtml" href="https://www.example.com/url/to/amp/document.html">`

Removing this link will essentially "disable" AMP cache.

No. While you'll get the optimized page loading order that AMP provides, without the `amphtml` link you will not get:

- AMP icon in Google search
- Chance to appear in AMP specific features such as Top Stories Carousel
- Google will not be able to pre-fetch your content. Meaning worse user experience for people who find your site through Google on a mobile phone.

Bottom line, web cache is the core aspect of AMP project and the benefits of using AMP without cache are greatly reduced.

*Relevant side note, from what I was told currently the AMP library does not play nice with some other JavaScript libraries. If you have such a use case, you can reach to the AMP team for more details.*

## Fixing the link

Even though the web cache sounds a bit scary, I can clearly see the benefit of it. I probably would have never made such a big deal about AMP, has the linking experience been half decent.

At the very list I want to very easily:

1. Click through to the original article ( not hosted on Google)
1. Copy the link to the original article, so I can share it through any internet connected device

I think I did a decent job communicating this concern. Paul and Malte assured me that they understood the problem and are confident that they can find a solution that will work for everyone.

That being said, I am not sure if "fixing" the link is their top priority. Personally, I will not feel 100% comfortable with AMP until this issue is resolved.

**In my mind the URL is the cornerstone of the web and it must be cherished and protected**.

## WordPress Integration

A lot of my pain with AMP came not from the AMP project itself, but rather from miss-understanding of how AMP plugin worked in WordPress. Long story short, it sort of worked like a new blank theme that stripped out most of the things that I had in place, such as analytics and ads scripts.

Some [Github issues](https://www.alexkras.com/google-may-be-stealing-your-mobile-traffic/#comment-55326) were created on WordPress AMP plugin, as a result of my original post, so things might get better in the future.

Malte mentioned that WordPress was a partner in the AMP project, although I am not sure what role they are playing.

What was interesting to me is that it appeared that Google worked very closely with major publishers, such as BBC and Daily Mail, to make sure that they were happy with the AMP experience.

My guess is that the WordPress integration was not monitored as closely, even though that Google team is aware of a number of issues with that plug-in.

As AMP was gaining steam, more and more small time WordPress publishers (such as myself) enabled AMP support and began participating in the AMP echo system. As WordPress AMP pages began showing up in Google search results, a number of confused and upset users (like myself two weeks ago) began to grow, making Google look more evil then they might have actually been.

While WordPress integration is not a fault of Google directly, I think it is very important for the success of the AMP project to fix the WordPress integration.

## Fat bar at the top

I didn't get to bring up one more concern expressed in my original article. Google presents a thick bar at the top of the AMP view, that has the close (x) button and the URL of the original source. It is fixed at the top and takes up roughly 10-15% of overall screen.

I did not bring up because I forgot :), but also because I can see it as a solution to the link issue. For example it can contain a button to allow coping the original URL.

## Conclusion

I don't think that Google set out to steal our traffic. In Malte's own words, from the start Google has been very careful to construct a project in such a way that publishers maintain full control of their content. Stealing content, is exact oposite of what they are trying to achieve.

At the same time, I don't think the words "full control" and AMP go together.

When I've first learned of AMP I assumed it to be a smaller and optimized subset of existing Web. As I learned more about a project, it appears to be it's own thing. Serving as a new application, created on top of the existing web. It functions similarly, but at the same time creates a number of different paradigms.

I am keeping my WordPress AMP turned on. With all the concerns and issues with the AMP project and the WordPress AMP plug-in, it AMP gets one thing right - **loads content really fast on mobile devices**. For that, a lot of little things can be (temporarily) forgotten.

At the same time, I hope that people who chose to participate in the AMP echo system will understand of the trade-offs involved and make an informed decision.

The link concerned, can be addressed short term by optimizing AMP view (just like the big publishers are doing now). 

Here is the list of suggestions on how to optimize AMP pages from my original article:

1. Make sure your Analytics tracking code is properly installed
1. Make sure you have a header that points back to your main site
1. If your site has a menu, make sure it is visible in the AMP version
1. Consider adding a link at the top of your AMP page, giving user an option to visit the original post or make the header of the post clickable
1. Make sure your ads and other promotional material is properly integrate into the AMP version

Last but not least, the AMP project appears to be in good hands. Both Paul and Malte appeared to be very open to constructive criticism and discussing how AMP project can be improved. If you have any feedback on the AMP project please make sure to let them know via [GitHub Issues](https://github.com/ampproject/amphtml/issues/new), Stack Overflow, or the AMP mailing list. Link to alls can be found under the [Support section of the AMP site](https://www.ampproject.org/support/faqs/).  
