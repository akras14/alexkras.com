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
1. Copy the link to the original article, so I can share it through any medium

I think I did a decent job communicating this concern and Paul and Malte assured me that they understand the problem and are confident that the problem can be solved.

While I appreciate their positive words, I did not get a feeling like they are actively working on a solution or that it is their top priority. Personally, I will not feel 100% comfortable with AMP until this issue is resolved. In my mind the URL is the cornerstone of the web and it must be cherished and protected.
 
