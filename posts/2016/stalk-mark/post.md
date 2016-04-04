## Part 1. A Naive Dream

### The Dream

In late 2015, I finished reading [Automate the Boring Stuff with Python](http://www.alexkras.com/review-automate-the-boring-stuff-with-python-by-al-sweigart/) and was very inspired to try to automate something in my life.

At the same time, I have been always fascinated by Mark Zuckerberg - Bill Gates of our time. A lot of people love to hate on Mark, but I actually like the guy. Sure he got lucky in life, but at the same time he is doing something right for Facebook to continue to stay successful.

In any case, one day I had a "brilliant" idea. **What if I write a script that would follow Mark's public posts and send me a text whenever he posted something new? Then I can be the first guy to comment on his post.** 

**After a while Mark would notice my comments and would begin to wonder "Who is this guys that is always posting meaningful responses to all of my posts?". Then he would invite my wife and me to his house for dinner and our kids will become friends. :)**

So, without further ado I got to work.

I've briefly considered using Facebook APIs to get notified on Mark's posts. I've had mixed experience with APIs in the past, hitting rate limits pretty quick and other related problems. Plus I wanted to use my [Automate the Boring Stuff with Python](http://www.alexkras.com/review-automate-the-boring-stuff-with-python-by-al-sweigart/) knowledge :)

So I went the other route, and wrote a Selenium script (which was really easy to do using [selenium](http://selenium-python.readthedocs.org/) module in Python) that would:

1. Log in to Facebook
2. Use current timestamp as the time of last post
3. Keep checking every 60 seconds if Mark has posted a new post
4. Send me a Text using [Twilio API](https://github.com/twilio/twilio-python), with a link to the new post

I happen to own a small server, so I set the script to run indefinitely in a headless browser ([PhantomJS](http://phantomjs.org/)) and began to wait.

### Paradise Lost

It took a couple of days for Mark to post something and I began to get worried that my script did not work. 

At some point I had to go to a post office. On my way back I've parked my car, checked my phone and saw a new SMS text from my script. My heart started to beat really fast and I rushed to open the link. I soon realized that the post took place 5 minutes ago and I missed the notification when I was driving. By now the post already had thousands of comments...

Oh well, I thought, there is always the next time. Sure enough within a day I had another text. This time it was within under 1 minute from the original post. I quickly open the link, only to discover that Mark's post already had close to 100 comments.

Now don't get me wrong, I am not stupid. I knew that Mark's posts were popular and would get a lot of comments. 

I even tried to estimate the rate at which people were posting replies. I've looked through Mark's older posts and saw some posts with tens of thousands of comments. So if you take 10000 comments and divide by 24 hours, then divide by 60 minutes, you get about 7 posts per minute.

What I didn't realize in my estimate is that those comments were not evenly distributed in time and that I had a very small chance of being the first to comment.

I knew that I was loosing my dream and I consider my options :)

I could set my script to run more often than every 60 seconds, to give myself an early warning. By doing so I would risk showing up on Facebook's radar as a spammer and it just didn't feel right for me to bombard their server that much.

Another option that I considered was to try to make an automated reply, in order to be one of the first people to comment. This approach, however, would defeat the purpose of saying something meaningful and would not help me to become friends with Mark. Sure, I could do it to prove the point, but I wasn't out to prove anything.

I've decided against both of these ideas and admitted my defeat. I've also realized, that I could turn this (failed) experiment into an interesting Data Exploration project.

## Part 2. Data Analysis

### Scraping

Having made a big error in my estimate of the rate at which people were replying to Mark, I was curious to explore what and when people were saying. In order to do that, I needed a data set of comments. 

Without putting much thought into it, I decided to scrape [one of Mark's most recent posts at the time](https://www.facebook.com/zuck/posts/10102557276035121).

<div id="fb-root"></div><script>(function(d, s, id) {  var js, fjs = d.getElementsByTagName(s)[0];  if (d.getElementById(id)) return;  js = d.createElement(s); js.id = id;  js.src = "//connect.facebook.net/en_US/sdk.js#xfbml=1&version=v2.3";  fjs.parentNode.insertBefore(js, fjs);}(document, 'script', 'facebook-jssdk'));</script><div class="fb-post" data-href="https://www.facebook.com/zuck/posts/10102557276035121" data-width="500"><div class="fb-xfbml-parse-ignore"><blockquote cite="https://www.facebook.com/zuck/posts/10102557276035121"><p>Merry Christmas and happy holidays from Priscilla, Max, Beast and me! Seeing all the moments of joy and friendship...</p>Posted by <a href="https://www.facebook.com/zuck">Mark Zuckerberg</a> on&nbsp;<a href="https://www.facebook.com/zuck/posts/10102557276035121">Friday, December 25, 2015</a></blockquote></div></div>

My first approach was too try to modify my notification script to:

1. Log in to Facebook
2. Go to the post that Mark has made
3. Click on "Show More Comments" link, until all comments were loaded
4. Scrape and parse the HTML for comments

Once again I under estimated the scale of the operation. There were just too many comments (over 20,000) and it was too much for a browser to handle. Both Firefox and PhantomJS continued to crush without being able to load all of the comments.

**I had to find another way**

I proceeded to examine how **View more comments** requests were made using Network Toolbar in Chrome Developer Tools. Chrome allows you to right click on any request and to copy it as CURL via "Copy as cURL" option. 

<img src="http://www.alexkras.com/wp-content/uploads/curl.png" alt="curl" width="990" height="491" class="aligncenter size-full wp-image-1143" />

I've ran the resulting CURL command in my terminal, and it returned some JSON. BINGO!

At that point all I had to do was to figure out how pagination of comments was done. Which turned out to be a simple variable in the query of the request, which acted as a pointer to the next set of comments to fetch.

I've converted the CURL command to a Python request code via [this online tool](http://curl.trillworks.com/).

After that I wrote a script that would:

1. Start at pagination 0
2. Make a comments request
3. Store it in memory
4. Increment the pagination
5. Sleep for a random amount of time from 5 to 10 seconds
5. Repeat the loop, until no more comments were found
6. Save all of the comments to a JSON file

I've ended up with an 18Mb minimized JSON file, containing about 20,000 comments.

### Analyzing the data

#### First I looked at the distribution of comments over time. 

As can be seen in the two plots bellow, it looked a lot like exponential decay, with most of the comments being made in the first two hours. 

**First Two Hours**
<img src="http://www.alexkras.com/wp-content/uploads/time-to-comment-minute.png" alt="time-to-comment-minute" width="393" height="281" class="aligncenter size-full wp-image-1133" />

**First 24 Hours**
<img src="http://www.alexkras.com/wp-content/uploads/time-to-comment-hour.png" alt="time-to-comment-minute" width="393" height="281" class="aligncenter size-full wp-image-1136" />

First 1500 comments were made within first 10 minutes. No wonder I had a hard time making it to the top.

#### Next I wanted to see what people were saying.

I created a word cloud of most commonly used keywords in comments using a python library called (surprise, surprise) - [Word Cloud](https://github.com/amueller/word_cloud).

<img src="http://www.alexkras.com/wp-content/uploads/facebook-word-cloud.png" alt="facebook-word-cloud" width="2000" height="2000" class="aligncenter size-full wp-image-1134" />

Looking at the word cloud I realized that I might have picked the wrong day to do this experiment. Most of the people responded in kind to Mark's wishes of Merry Christmas and Happy New Year. That was great news for Mark, but kind of boring from the data exploration stand point.


#### Digging Deeper


After I finished the word cloud I've spent WAY TOO MUCH TIME trying to gain a deeper understanding of the data.

The data set turned out to be a bit too big for me to iterate on it quickly and all of the positive comments created too much noise. 

I've decided to narrow down the data set by removing all comments with any of the following [word stems](https://en.wikipedia.org/wiki/Word_stem). A word stem is simply a shortest version of the word that still makes sense. For example by removing comments that have a word **thank** in it, I was able to remove both the comments with the words **thank you** as well as the comments with the word **thanks**. I've used [nltk](http://www.nltk.org/api/nltk.stem.html) library to help me convert my words to stems.

I've organized the stems by a type of comment that they usually belonged to:

- Happy New Year Wishes
    + new
    + happ
    + year
    + wish
    + bless
    + congrat
    + good luck
    + same
    + best
    + hope
    + you too
- Comment on Photo of the Family
    + photo
    + baby
    + babi
    + beautiful
    + pic
    + max
    + family
    + famy
    + cute
    + child
    + love
    + nice
    + daughter
    + sweet
- Thanking Mark for creating Facebook
    + thank
    + connect
    + help

After removing all of the typical comments, I've ended up with  2887 "unusual" comments.

#### Digging Even Deeper

I've also recently finished reading [Data Smart](http://amzn.to/1S0lYdP), from which I learned that [Network Analysis](https://en.wikipedia.org/wiki/Network_theory) can be used to identify various data points that belong together, also known as clusters.

One of the examples in [the book](http://amzn.to/1S0lYdP) used [Gephi](https://gephi.org/) - an amazing software that makes cluster analysis very easy and fun. I wanted to analyze the "unusual" comments in Gephi, but first I had to find a way to represent them as a Network.

In order to do that, I've:

1. Removed meaningless words such as "and" or "or" (also known as [stop words](https://en.wikipedia.org/wiki/Stop_words)) from every comment using [nltk](http://www.nltk.org/) library
2. Broke remaining words in every comment into an array (list) of [word stems](https://en.wikipedia.org/wiki/Word_stem)
3. For every comment calculated intersection with every other comment
4. Recorder a score for every possible intersection
5. Removed all intersection with a score of 0.3 or less
6. Saved all comments as nodes in Gephi graph and every intersection score as an undirected edge

By now you might be wondering how the intersection score was calculated. You may also wonder what the heck is Gephi graph, but I'll get to it a bit later.

**Calculating Intersection Score**
 Let say we have two comments

```python
["mark", "love"] # From "Mark, I love you"
# and
["mark", "love", "more"] # From "Mark, I love you more"
```

We can find the score as follows:

```python
def findIntersection(first, second):
    intersection = first & second               # Find a sub set of words that is present in both lists
    intersectionLength = len(intersection)      # Words both comments have in common
    wordCount = len(first) + len(second)        # Total length of both comments
    if wordCount == 0:                          # Corner case
        return 0
    else:
        return (intersectionLength/wordCount)   # Intersection score between two comments
```

So for our example above:

1. Intersection between two comments is `["mark", "love"]` which is 2 words
2. Total length of both comments is 5 words
3. Intersection score is 2/5 = 0.4

*Note: I could have used average length of two comments (so 2+3/2 = 2.5) instead of total length (5), but it would not have made any difference since the score was calculated similarly for all of the comments . So I decided to keep it simple.*

Once I had all of intersection calculated I saved all comments in the nodes.csv file, that had the following format: 

```csv
Id;Label
1;Mark, I love you
```

I've saved all intersection in the edges.cvs file, that had the following format:

```csv
Source;Target;Weight;Type
1;2;0.4;"Undirected"
```

**Analyzing the Network**

This was all that was needed to import my data into Gephi as a Network Graph. You can read more about Gephi file formats [here](https://gephi.org/users/supported-graph-formats/spreadsheet/) and [this video](https://www.youtube.com/watch?v=kbLFMObmLNQ) provides a good introduction to Gephi and how it can be used.

Once I imported my data, into Gephi I've run a network analysis algorithm called "Forse Atlas 2", which resulted in the following network Graph.

I've manually added the text in red to summarize some of the clusters. If you click on the image, you will be taken to a full screen representation of the graph. It is pretty big, so you might have to zoom out and scroll for a while before you see some data.

<a href="http://alexkras.com/demo/comment-network/" target="_blank" rel="attachment wp-att-1135"><img src="http://www.alexkras.com/wp-content/uploads/min-network.png" alt="min-network" width="1024" height="1024" class="aligncenter size-full wp-image-1135" /></a>

**Some Notes on Results**

I was really happy to see my approach finally working (after many days of trying).

I have been starring at those comments for a long time and I've seen some references to "money". Therefore, I was not surprised to see a couple of clusters asking Mark "Where is my Money?".

I was very surprised, however, to see a cluster of comments mentioning a specific number - 4.5 million to be exact. I had no idea where this number was coming from, but a quick Google search pointed me to [this hoax](http://www.snopes.com/mark-zuckerberg-facebook-giveaway-scam/). Turns out a lot of people were duped into believing that Mark would give away 4.5 million to 1000 lucky people. All you had to do was to post a "Thank you" message of sorts.

Other than that, I didn't see anything very interesting. There were some spammers and some people asking Mark to ban some people form Facebook. Some aggression towards Mark and a lot more of general types of comments that I did not filter out.

I've also noticed some weaknesses in my approach. For example there were two clusters around the word "precious". It was probably caused by removing relationships that did not have intersection score of at least 0.3. Since I did not use the average length for two comments, the threshold of 0.3 really meant that the two comments were at least 60% similar, and it was probably too high and caused the error. On the flip side it has helped to reduce the number of edges, focusing on the most important connections.

Please let me know in the comments, if you find anything else note worthy or if you have suggestions on how intersection scores can be improved.

## Conclusion

It is hard being a celebrity.

I started this journey naively assuming that I can get Mark's attention by simply posting a comment on his timeline. I did not realize the amount of social media attention an average celebrity gets.

It would probably take a dedicated Data Scientist working full time just to get insight into all of the comments that Mark gets. While Mark can afford to hire such a person, my bet is that he is using his resources for more meaningful things.

That being said, this has been a great learning experience for me. [Gephi](https://gephi.org/) is a magical tool, and I highly recommend checking it out.

If you want some inspiration for automating things, I highly recommend reading [Automate the Boring Stuff with Python](http://www.alexkras.com/review-automate-the-boring-stuff-with-python-by-al-sweigart/).

If you are looking for a good entry level text on Data Science, I found [Data Smart](http://amzn.to/1S0lYdP) to be an informative read, although hard to follow at times.


Also note that I've destroyed all of my data sets to comply as best as I can with Facebook's Terms of Service. Scraping content without permission is also against Facebook's Terms of Service, but I've avoided thinking about it until after I've done all of my analysis. 

I am hoping that Facebook will over look my transgression, but wanted to make sure I don't send anybody else down the wrong path without a proper warning.

[If all else fails, you can always follow me on Twitter :)](https://twitter.com/akras14)
