## Part 1. A Naive Dream

### The Dream

In late 2015, I finished reading [Automate the Boring Stuff with Python](http://www.alexkras.com/review-automate-the-boring-stuff-with-python-by-al-sweigart/) and was very inspired to try to automate something in my life.

At the same time, I have been always facinated by Mark Zuckerberg - Bill Gates of our time. A lot of people love to hate on Mark, but I actually like the guy. Sure he got lucky in life, but at the same time I believe he is doing something right for Facebook to continue to stay sucseful.

In any case, ond day I had a briliant idea: what if I write a script that would follow Mark's public posts on Facebook and send me a text whenever he posted something. Then I can rush to my phone and be the first guy to comment on his post. After a while Mark would notice my responses, and would beging wondering "who is this guys always posting meaningful comments on all my posts". After a while he would take interest in me, would invite me and my wife to his house for dinner, and us and our children will become friends. :)

So, without further ado I got to work.

I've briefly considerered trying to use Facebook API to get notified on Mark's posts, but had mixed experience with APIs in the past, hitting rate limites etc. Plus I just didn't want to spend too much time trying to figure it out, and I wanted to use my "Automate the Boring Stuff with Python" knowledge :)

So I went the other route, and wrote a Selenium Script (which was really easy to do using [selenium](http://selenium-python.readthedocs.org/) module in Python) that would:

1. Log in to Facebook
2. Use current timestapm as the time of last post
3. Keep checking every 60 seconds if Mark has posted a new post
4. Send me a Text using [Twilio API](https://github.com/twilio/twilio-python), with a link to the new post

I happend to own a small server, so I set the script to run indefinitely in a headless browser (PhantomJS) and began to wait.

### Paradise Lost

It took a couple of days for Mark to post something, and I began to get warried that my script did not work properly. At some point I had to go to a post office. On my way back, I've parked my car, checed my phone a saw an SMS text from my script. My heart started to bit really fast, and I rushed to open the link. Only to realize that the post happend 5 minutes ago, and I missed the notification when I was driving. By that point, post already had thousands of comments...

Oh, well I thought there is always a next time. Sure enought, within a day I had another text. This time I was within under 1 minute from the original post. I quickly open the link, only to discover that Mark's post already had close to 100 comments.

Now don't get me wrong, I am not stupid. I knew that Mark's posts were popular, and would get a lot of comments. I've even went as far as try to estimate the rate at which people has posted. I've looked at his older posts, and saw some posts with 10ths of thousands of comments, that were published about 24 hours ago. So if you take 10000 comments and divide by 24 hours, then divide by 60 minutes, I was expecting to have about 6 posts in the first minute. It's a lot, but I thought I could rise above those 6 with my meaningful comments. 

What I didn't realize in my estimation is that those comments were not evenly distributed in time, and that a lot of them were scewed towards the time when Mark first made the post.

At that ponit I've considerered my options. I could have set my script to run more often than every 60 seconds. Then I was risking to show up on Facebook radar for pinging their site too much, and it just didn't feel right.

Another option I considered, is to try to make an automated post. It would defete the purpose of saying something meaningful, but at least I'd get to prove the point.

I've decided against that idea. After all, I never wanted to spam, I just wanted help to try to learn about Mark's new posts, so I can makre a real comment.

At this point, I decided to cut my lossses and try to turn this (failed) experiment into a Data Exploaration project.

## Part 2. Data Analysis

### Scraping

I was curious to see with what and when people were replying to Mark's post. In order to do that, I needed a data set of a post, and some comments. 

Without putting much thought into it, I decided to scrape [one of the most recent posts](https://www.facebook.com/zuck/posts/10102557276035121) (at the time) that Mark has made.

My first approach was too try to modify my script to:

1. Log in to Facebook
2. Go to the post that Mark has made
3. Click on "Show More Comments" link, until all comments are loaded
4. Scrape and parse the HTML for comments

Once again I under estimate the scale of operation. There were just too many comments (over 20,000) and it was too much for a browser to handle (both Firefox and PhantomJS continued to crush, after getting some number of comments).

**I had to find another way, if I wanted to scrape most of the comments.**

I proceded to examing how "View more comments" requests are made in my Chrome Developer Tools - Netwoork Toolbar. One of the options that available there, if you right click on the request is to "Copy as cURL". I tried to run the CURL command in my terminal, and it returned some JSON.

{{Image Of Copy As CURL}}

At that point all I had to do, is to figure out how pagination on comments was done.

I've converted the CURL command to Python reuqest code via [this online tool](http://curl.trillworks.com/).

After that I wrote a script that would:

1. Start at 0 pagination
2. Make a comment requests
3. Store it in memory
4. Increment the pagination
5. Repeat the loop, until no more comments were found
6. Save all of the comments to a JSON file

I've ended up with an 18Mb minimized JSON file, containing about 20,000 comments.

### Analyzing the data



