#  Notes from the 2016 Chrome Dev Summit

Originally posted on [http://www.apixio.com/technical-post/notes-from-the-2016-chrome-dev-summit/](http://www.apixio.com/technical-post/notes-from-the-2016-chrome-dev-summit/)

Two weeks ago I got to attend the Chrome Dev Summit, an annual two-day conference
hosted by Google where they announced latest developments relevant to the web
technology. Here are my full notes from this conference. Since there was so
much information presented, I decided to organize it by subject, instead of
chronological order of talks presented.

[You can watch all of the recorded
talks.](https://www.youtube.com/playlist?list=PLNYkxOF6rcIBTs2KPy1E6tIYaWoFcG3uj)

## Statistics and Charts

  * Over 2 Billion Chrome Browsers worldwide across desktop and mobile
  * 53% of users say they will leave a site if it’s not loaded in 3 seconds or less
  * Mobile Stats
    * 19 seconds – average mobile page load time
    * 77% of mobile sites take 10+ seconds to load
    * 214 server requests per mobile web page
  * Housing.com reports user acquisition costs – $3.75 mobile install vs $0.07 Progressive Web App

<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">The mobile web is no longer a subset of the web. It is the web. <a href="https://twitter.com/samccone">@samccone</a>  <a href="https://twitter.com/hashtag/ChromeDevSummit?src=hash">#ChromeDevSummit</a> <a href="https://t.co/i6LjPYKxHE">pic.twitter.com/i6LjPYKxHE</a></p>&mdash; Sam Richard (@Snugug) <a href="https://twitter.com/Snugug/status/796883029641728001">November 11, 2016</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

## Progressive Web App

When I attended Chrome Dev Summit for the first time in 2014, my key complain
was “this is great, but all of the talks are about the mobile web.” This year,
Google pushed to get rid of this mentality, by calling everything (mobile and
desktop) a **Progressive Web App**.

Progressive Web App is a newish term, that according to [Mozilla Developer
Network (MDN)](https://developer.mozilla.org/en-US/Apps/Progressive) means:

  * Discoverable
  * Network Independent (Even offline)
  * Responsive
  * Installable
  * Works for every browser
  * Safe
  * Linkable
  * Re-engageable

<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">Progressive Web Apps as a term is new but the concept has been around for a very long time. Look at HTA <a href="https://twitter.com/hashtag/chromedevsummit?src=hash">#chromedevsummit</a> <a href="https://twitter.com/patrickkettner">@patrickkettner</a></p>&mdash; Abraham Williams (@abraham) <a href="https://twitter.com/abraham/status/797228227945111553">November 12, 2016</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

**Progressive Web Apps takeaways**

  * Progressive Web App != Single Page Application
  * Progressive Web Apps = Smaller user acquisition funnel and faster updates (no need to wait for the App Store)
  * Older technology can be leveraged to provide Progressive Web App experience on all platforms today. If you are interested in supporting various platforms (including Mobile Safari) I highly recommend watching a talk by Patrick Kettner, Edge PM, Microsoft – [The “Progressive” in Progressive Web Apps](https://youtu.be/ARkPBm6AcNA?list=PLNYkxOF6rcIBTs2KPy1E6tIYaWoFcG3uj)

## Tech

**Service Workers**

Service Workers (not to be confused with Web Workers) are a big deal. [MDN
defines Service Workers as follows](https://developer.mozilla.org/en-
US/docs/Web/API/Service_Worker_API):

Service workers essentially act as proxy servers that sit between web
applications, and the browser and network (when available). They are intended
to (among other things) enable the creation of effective offline experiences,
intercepting network requests and taking appropriate action based on whether
the network is available and updated assets reside on the server. They will
also allow access to push notifications and background sync APIs.

I first learned of Service Workers when I attended Chrome Dev Summit in 2014.
At the time the support was limited to the latest Chrome. Things have improved
since then, with Chrome, Firefox and Opera having a full support, and Edge
actively working to add support.

Safari is the only browser without indication of planning to support Service
Worker, with only Mobile Safari being a big deal, since Desktop users have
other options.

<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">&quot;Hundreds of millions of pages are loaded from ServiceWorker per day in Chrome&quot; <a href="https://twitter.com/hashtag/ChromeDevSummit?src=hash">#ChromeDevSummit</a></p>&mdash; Eric Lawrence (@ericlaw) <a href="https://twitter.com/ericlaw/status/797214344773668864">November 11, 2016</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

**Service Worker takeaways**

  * Service Worker Precipices <https://serviceworke.rs/>
  * Offline Google Analytics Library – Pushes Events after user gets back online <https://www.npmjs.com/package/sw-routing>
  * Good library to get started with Service Workers – [sw-precache](https://github.com/GoogleChrome/sw-precache)
  * [Live coding session adding Service Worker to a page](https://youtu.be/X8EQSy-ajo4?list=PLNYkxOF6rcIBTs2KPy1E6tIYaWoFcG3uj)

**Web Assembly**

  * Latest Web Assembly info and step by step guide can be found at <http://webassembly.org/>
  * Interesting demo of how Web Assembly can be used today behind a flag (towards the middle of this talk) – [Advanced JS performance with V8 and Web Assembly](https://youtu.be/PvZdTZ1Nl5o?list=PLNYkxOF6rcIBTs2KPy1E6tIYaWoFcG3uj)
  * Web Assembly is on by default in early 2017

**HTTPS**

  * Sites with input fields (password, credit card etc) and no HTTPs are going to get big “Not Secure” warning on 01/2017
  * HTTPs usage report – it’s growing <https://www.google.com/transparencyreport/https/metrics/?hl=en>
  * Thanks [Let’s Encrypt](https://letsencrypt.org/)
  * Service Workers, Push and other APIs are ONLY available over HTTPs
  * [Full HTTPs Talk](https://youtu.be/iP75a1Y9saY?list=PLNYkxOF6rcIBTs2KPy1E6tIYaWoFcG3uj) and [Slides](https://t.co/L0E3vLhWrD)

**ES6+**

<blockquote class="twitter-tweet" data-lang="en"><p lang="ht" dir="ltr"><a href="https://twitter.com/hashtag/chromedevsummit?src=hash">#chromedevsummit</a>  JS Languaje Features <a href="https://t.co/CKu0uTM3VB">pic.twitter.com/CKu0uTM3VB</a></p>&mdash; Milton Yarleque (@myarleq) <a href="https://twitter.com/myarleq/status/797207603717828608">November 11, 2016</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

  * V8 has Great coverage – Chrome and Node.js 7
  * Async/Await available behind –harmony-async-await in Node.js 7 and Canary

**Web Manifest**

MDN [defines Web Manifest](https://developer.mozilla.org/en-
US/docs/Web/Manifest) as follows:

The web app manifest provides information about an application (such as name,
author, icon, and description) in a text file. The purpose of the manifest is
to install web applications to the homescreen of a device, providing users
with quicker access and a richer experience.

Web Manifest is a must have for any installable (add to home screen etc)
Progressive Web App.

  * Web tool to [auto generate Web Manifest file](https://webmanife.st/)
  * CLI tool to [help generate Web Manifest](https://www.npmjs.com/package/manifest-json)

**Polymer**

  * Blessed by numerous speakers as one of the few performant frameworks (in addition to preact) that can be used to create Progressive Web Apps
  * Polymer App Toolbox – [Collection of components to build Progressive Web Apps](https://www.polymer-project.org/1.0/toolbox/)
  * polydev – Polymer [Chrome Dev tools extension](https://github.com/PolymerLabs/polydev)
  * polyperf – [Simple web page performance harness](https://github.com/PolymerLabs/polyperf)

**Accelerated Mobile Pages (AMP)**

<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">Announced today: AMP can now prewarm caches for onward journeys in all browsers (including Safari!!!) <a href="https://twitter.com/hashtag/ChromeDevSummit?src=hash">#ChromeDevSummit</a></p>&mdash; Malte Ubl (@cramforce) <a href="https://twitter.com/cramforce/status/797151433170632704">November 11, 2016</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

  * Can help speeding up the initial Progressive Web App load, until Service Worker cache kicks in
  * Allows for a proper AMP to PWA hand off
  * Full Talk – [From AMP to PWA – the best of both worlds](https://youtu.be/M_ZCgbEGyHY?list=PLNYkxOF6rcIBTs2KPy1E6tIYaWoFcG3uj)

**Push Notifications**

  * Over 500,000 Domains using Push API
  * With Service Worker can push notification, long after a browser tab is closed

**Local Storage**

  * Use it as local cache to get a huge performance win
  * Full talk dedicated to the subject, with some Browser specific numbers – [The State of Storage](https://youtu.be/gq80Y5-ZJdg?list=PLNYkxOF6rcIBTs2KPy1E6tIYaWoFcG3uj)

**Preload**

  * You can use &lt;link rel=”preload” (Chrome only) to ask Chrome to pre-fetch some data

**Credentials API**

  * Proposal to let browser maintain Users being Authenticated with various sites
  * [Full talk](https://youtu.be/NJ-sphu2DqQ?list=PLNYkxOF6rcIBTs2KPy1E6tIYaWoFcG3uj)

**Payments API**

<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">The Payment Request API gets me so hyped. Imagine what it could do for subscription content! <a href="https://t.co/LsoyVKeUXh">https://t.co/LsoyVKeUXh</a> <a href="https://twitter.com/hashtag/ChromeDevSummit?src=hash">#ChromeDevSummit</a> <a href="https://t.co/RwY4IyscYM">pic.twitter.com/RwY4IyscYM</a></p>&mdash; Rachel🦄Nabors (@rachelnabors) <a href="https://twitter.com/rachelnabors/status/796812511106371585">November 10, 2016</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

  * Proposal to let browser store payment information and simplify payment process
  * [Full Talk](https://youtu.be/U0LkQijSeko?list=PLNYkxOF6rcIBTs2KPy1E6tIYaWoFcG3uj)

**Facial Recognition API**

  * It’s coming

**Canvas Capture API**

  * canvas.captureStream available in Firefox now

**Firebase**

  * Firebase hosting supports HTTP2 out of the box

**Houdini**

  * New proposal to simplify CSS?
  * [Slides](https://speakerdeck.com/surma/houdini-breakout-session)

## Tools

**Chrome Dev Tools**

  * Full talk – [Debugging The Web](https://youtu.be/HF1luRD4Qmk?list=PLNYkxOF6rcIBTs2KPy1E6tIYaWoFcG3uj)
  * Can now debug Node.js code in Dev Tools
  * Highlighting unused CSS
  * Multiple break points in the same line (i.e. Promise chain)
  * Intelligent multi-line entry in Console (line Node console) no more need for Shift+Enter
  * Better call stack

**Lighthous**

Lighthouse analyzes web apps and web pages, collecting modern performance
metrics and insights on developer best practices.

Cool tool to analyze your website’s performance. Check it out:
<https://github.com/GoogleChrome/lighthouse>

## Optimization

<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">Takeaways from <a href="https://twitter.com/hashtag/ChromeDevSummit?src=hash">#ChromeDevSummit</a>: Virtually every speaker has mentioned this and &quot;send less JavaScript.&quot; <a href="https://t.co/jRo6g8h62h">pic.twitter.com/jRo6g8h62h</a></p>&mdash; Eric Lawrence (@ericlaw) <a href="https://twitter.com/ericlaw/status/797164174837092352">November 11, 2016</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">Loading your JavaScript bundle over a 2G connection <a href="https://t.co/6luaY8lFFX">pic.twitter.com/6luaY8lFFX</a></p>&mdash; Changelog (@changelog) <a href="https://twitter.com/changelog/status/797093069732585472">November 11, 2016</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

  * **SHIP LESS JAVASCRIPT**
  * **Server Side Rendering** still outperforms most highly optimized JavaScript Apps
  * TypeScript + Closure Compiler provide type safe minification. a.something()becomes a.b()
  * Only 10% of apps use code splitting
  * Majority of Web Apps use WebPack
  * WebPack supports [Code Splitting](https://webpack.github.io/docs/code-splitting.html)
  * [RAIL Model](https://developers.google.com/web/fundamentals/performance/rail)
    * Response
    * Animation
    * Idle
    * Load
  * [RPRL Pattern](https://www.polymer-project.org/1.0/toolbox/server)
    * Push critical resources
    * Render initial route
    * Pre-cache remaining routes
    * Lazy-load remaining routes on demand
  * [Preact](https://github.com/developit/preact) is blessed as only other (in addition to Polymer) performant enough framework to build Progressive Web Apps

## Browser Support

  * [Search for bugs](https://developers.google.com/web/feedback/browser-bug-searcher) across all major browsers
  * Star bugs you care about to move the web forward
  * If you use it, browser will support it!

**Apple**

<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">On <a href="https://twitter.com/hashtag/ChromeDevSummit?src=hash">#ChromeDevSummit</a> there are people from Microsoft, Firefox, Opera... but no Apple. Do <a href="https://twitter.com/Apple">@Apple</a> remember Job&#39;s words: Write amazing Web apps? <a href="https://t.co/YqLJgRV1dd">pic.twitter.com/YqLJgRV1dd</a></p>&mdash; Valentyn Shybanov (@olostan) <a href="https://twitter.com/olostan/status/797253468373143553">November 12, 2016</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

  * Google, Mozilla, Opera, Samsung, Microsoft came to the [Browser Vendor panel](https://youtu.be/3VV-9_dCYuM?list=PLNYkxOF6rcIBTs2KPy1E6tIYaWoFcG3uj), Apple decline to participate
  * To be fair an Engineer from Apple was present at the Summit and [made himself available](https://twitter.com/jonathandavis/status/796903846437978113)

**Microsoft**

  * Progressive Web Apps will get **automatically ingested into Windows App Store**
  * Progressive Web Apps are top priority for MicroSoft for the next year
  * Edge Dev team hired some great people like [@auchenberg](https://twitter.com/auchenberg?lang=en) and [@rachelnabors](https://twitter.com/rachelnabors)

**FireFox**

  * Pretty much on board with everything that Google is proposing

**Brave**

<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">At <a href="https://twitter.com/hashtag/chromedevsummit?src=hash">#chromedevsummit</a> but not on Browser vendor panel -- <a href="https://twitter.com/brave">@Brave</a> is too small, apparently, even though they just asked about ads &amp; ad blocking.</p>&mdash; BrendanEich (@BrendanEich) <a href="https://twitter.com/BrendanEich/status/797253795927330816">November 12, 2016</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

  * Brendan Eich was pissed that he wasn’t invited to participate in the Browser Vendor panel 🙂

## Devices

<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">Serious <a href="https://twitter.com/hashtag/perfmatters?src=hash">#perfmatters</a> talk from <a href="https://twitter.com/slightlylate">@slightlylate</a> <a href="https://twitter.com/hashtag/ChromeDevSummit?src=hash">#ChromeDevSummit</a><br>Key reason mobile phones aren&#39;t as fast as computers is heat 🔥</p>&mdash; Nicolás Bevacqua (@nzgb) <a href="https://twitter.com/nzgb/status/796857229294997504">November 10, 2016</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

  * GREAT Talk on Mobile Web and the challenges that we are facing – [Progressive Performance](https://youtu.be/4bZvq3nodf4?list=PLNYkxOF6rcIBTs2KPy1E6tIYaWoFcG3uj)
  * The $700 iPhone in your pocket is NOT what next billion of people to come online will be using
  * Placing crappy mobile phone on an ice pack improves performance by 15%
  * The reason mobile phones can’t keep up is heat (seriously watch that talk)
  * Current state of Mobile Web is not good. We must put in the work to make it work for the next billion of users

## Examples of Progressive Web Apps

<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">Code splitting and preloading for the win <a href="https://twitter.com/flipcart">@flipcart</a> <a href="https://twitter.com/hashtag/ChromeDevSummit?src=hash">#ChromeDevSummit</a> <a href="https://t.co/niFuiqH4uy">pic.twitter.com/niFuiqH4uy</a></p>&mdash; Alex Kras (@akras14) <a href="https://twitter.com/akras14/status/797169715487477760">November 11, 2016</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset=”utf-8”></script>

  * Lyft implemented a Web only version of their app, no download required. Think about it. _Android Chrome Only_ – <https://ride.lyft.com/>
  * NASA’s <https://code.nasa.gov/> was re-implemented to be a Progressive Web App
  * From the [The “Progressive” in Progressive Web Apps](https://youtu.be/ARkPBm6AcNA?list=PLNYkxOF6rcIBTs2KPy1E6tIYaWoFcG3uj) talk – good example of Progressive Web App that supports wide range of devices, including Mobile Safari <https://hushlittleba.by/>
  * Other examples included
    * Flipcart
    * Housing.com
    * Weather Channel
    * Mic
    * Cnet
    * Alibaba

## Conclusion

I really enjoyed Chrome Dev Summit, even though it was a long two days.

It seems that Google is hyper aware of the current web trends. Modern web is
not ready for the mobile revolution and Google is very interested in changing
that status quo.

Even if your current business needs are not affected by the developing mobile
market, try to keep two things in mind.

  1. Business needs can change, sometimes really fast
  2. There are a number of benefits that Progressive Web Apps could provide for businesses that are not targeting the Mobile web at all (Caching, Push Notifications etc)

I think the Web will win if we all work together.

P.S. [We are hiring](http://www.apixio.com/join-apixio/)
