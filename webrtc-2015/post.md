## Kranky Geek 2015 - WebRTC conference
[http://www.krankygeek.com/](http://www.krankygeek.com/)

*Note: The [talk by Google](#google) is listed in the order that it appeared.*

## Brief Welcome
<iframe width="560" height="315" src="https://www.youtube.com/embed/Zl650wbirYE" frameborder="0" allowfullscreen></iframe>

### Tsahi Levi-Levent - bloggeek.me

- WebRTC very easy vs VOIP etc, nothing beats that.
- Continuous slow growth, not exponential.

## A closer look at the WebRTC UX/UI API

User interaction for real time communications is way different than dealing with typical web content and streaming media. Arin will cover best practices for incorporating WebRTC into your application for a smooth user experience.

*Note: I recommend watching this talk.*
<iframe width="560" height="315" src="https://www.youtube.com/embed/H7hAapxpsOY" frameborder="0" allowfullscreen></iframe>

### Arin Sime - webrtc ventures (Real time Weekly)

- Technology is cool, but users don't care (use easy metaphors like Skype in your browser).
- All users care about is experience
- Allow/Block Camera (for example) - what do you do if they block?
- How do you warn them, that you about to share their camera? How do you warn them even if they already gave the permission a month ago?
- Some UX considerations
	- Micro Interactions (minor things that users don't notice, but that make big difference)
	- Information Hierarchy (Structure and placement - symbolize importance)
	- Feedback (Feedback to the user, making it obvious what is going on)
- Make larger controls(buttons) for mobile apps
- Multi-party - put their picture if camera is paused, so you know who is speaking
- Provide feedback before and during on status of connection
	- Slow - let them know, that you can't support it
	- Mediocre - warn them that the video will be paused
	- Connection goes bad, you can pause the video, and still keep the audio
- Maintain focus, emphasize what is important but keep the other stuff in
- Everything matters even more with mobile
- Key point - WebRTC is much more than a video tag

## Application Chats

Hear first hand the choices & decisions an app dev faced with their WebRTC app, how they made them, what they did and what would they recommend you consider. Great quick speakers from Freshdesk, Wix.com and Skedans.


### Skedans

<iframe width="560" height="315" src="https://www.youtube.com/embed/7_34WfyOjx4" frameborder="0" allowfullscreen></iframe>

- Value - more than just browser to browser communication without plugin
- Very easy to set up real time app in peer to peer mode
	- But more than 4,5 parties need centeralized server
- Drone + Drone Operator + webRTC + Remote Audience = flight and control center

### FreshDesk

*Note: I recommend watching this talk.*
<iframe width="560" height="315" src="https://www.youtube.com/embed/d1KBSTaxmtE" frameborder="0" allowfullscreen></iframe>

- SF, 50K customers - democratize customer support - make it available to everybody
- Mission leads to the technology choices
- Types of Support
	- Voice 80%
		- Uses Twilio WebRTC solution
		- You want to provide pristine experience - How do you make sure audio is available without clunky installations?
		- That is where WebRTC comes to play - Customers:
			- Log in
			- Allow WebRTC
			- Ready to go - No implementations/installations required
		- Throw some JS on page and immediately customers can interact with agents
	- Chat
	- Video
- WebRTC both powerful and versatile
- Translate complicate technology into easy to use interface
- Q. How do you deal with browsers that don't support. A. Fall back to flash (which is not desirable)

### Wix.com - Build websites

*Note: I recommend watching this talk.*
<iframe width="560" height="315" src="https://www.youtube.com/embed/FV9VA4JhZjQ" frameborder="0" allowfullscreen></iframe>

- Wix.com helping people build websites - needs a lot of customer support
- Flash was problematic
- 2 types of users
	- Support Agents
	- Person building their site
- Use Twilio
	- They offered WebRTC so they jumped on it
	- Instant positive user feedback
	- Nice open platform (Chrome/Firefox)
	- Twilio allows to easily build custom call center solution
		- Python API
		- Alerts
		- Downtime
		- Custom Routing
		- Really easy to set up, no need to dig into internals (just voice for now)
		- Looking into customizing for screen sharing
		- No plug-ins to monitor, just keep Chrome up to date
		- Communication via web sockets
			- Open socket to Twilio
			- Another socket to update all updates inside Call Center Application
		- Very easy to roll back to Flash
- Watch out for difference in Chrome vs FF, test in both
- Flash is removed on Mobile, but WebRTC IS supported on Android
- Q. Do your customers use WebRTC. A. No, only agents use WebRTC. It's a bridge from Phone (Wix customer) line to WebRTC App (Wix agent). Works really well.
Using Twilio API

## IBM Bluemix: Mixing voice & data

In this demo, a video call (using the new Twilio video API) is held between a customer and a customer service agent. As the video call is happening IBM Watson Speech to Text service is transcribing the audio in real time. After the video call completes, Alchemy API is used to automatically determine which product the customer was giving feedback on and then determines the sentiment of that feedback. The corresponding product's feedback score, a number between 0 and 100, fluctuates based on this feedback. After the score is updated, Business Rules are invoked to determine if the product has crossed a threshold to automatically suggest a review of investment in the product. If the rules suggest a review, a process instance for a change in product investment is then started and managed by the Bluemix Workflow service. This creates a task for a buyer at the company. The buyer can then decide whether to ignore or go through with the review, thus completing the process.

<iframe width="560" height="315" src="https://www.youtube.com/embed/xkB0qiU6PGk" frameborder="0" allowfullscreen></iframe>

### Jeff Sloyer - IBM Bluemix

- WebRTC invaded the Doctors Office
- Real time transcribing - using Watson to transcribe WebRTC audio to text
- Bluemix - like Heroku with Watson access
- Built in 3 days
	 - WebRTC + BlueMix + Twilio - makes your life as a developer really easy
- There is NPM package for Watson
- Challenges
	- A lot of stuff not documented well
	- Issue for remote streams in Chrome vs FF
	- Multiple web-socket audio streams are hard
	- Getting the audio format right (Watson's docs didn't mentioned supported format at the time)
	- Personality of the patient *Note: some machine learning stuff, can't figure out until the call is over*
	- Scaling web-sockets
	- Spying on the media stream is hard and not well documented
	- Web-socket to Watson drooped a lot, had to write a re-try logic
- Q. Are you Hipaa compliant? BlueMix is compliant, encrypted, and spent a lot of time on that.

## What is Mozilla doing with Firefox?

WebRTC allows the sharing of screen content - Mozilla has some cool demos to share which highlight the power of WebRTC beyond the typical voice/video communications that we typically think of. Plus, we'll get an update on the continued progress of Firefox with WebRTC.

*Note: I recommend watching this talk.*
<iframe width="560" height="315" src="https://www.youtube.com/embed/WZhqWvFHGSo" frameborder="0" allowfullscreen></iframe>

### Nils Ohlmeier - Mozilla

- Canvas
	- Firefox allows using canvas as an input for your PeerConnection (think canvas instead of camera)
	- Available in FF 41
	- Expected to be live in FF 43
	- Replace Camera with Canvas as video input
	- Can do Camera to Canvas -> Do some magic on Canvas -> Stream to WebRTC
	- Gets more interesting
		- Multiple cameras to one Canvas and stream that
		- Can do a MCU
	- Demo
		- One [http://nils-ohlmeier.github.io/webrtc-landing/canvas_filter_demo.html](http://nils-ohlmeier.github.io/webrtc-landing/canvas_filter_demo.html)
		- Two [http://nils-ohlmeier.github.io/webrtc-landing/canvas_demo.html](http://nils-ohlmeier.github.io/webrtc-landing/canvas_demo.html)
- IPv6 support FF 42
- Support Interactive Connectivity Establishment (ICE) TCP FF 42  (Turned off by default, on in FF 43-44)
- Upcoming Audio Features
	- Audio performance improvements, especially on Windows
	- Support for stereo sound
	- Up 16 to 32 KHz Audio
	- Audio capture for screen sharing (FF43)
- More
	- Simulcast support
	- applyConstraind for gUM Media stream - **make lower resolution** FF43-44
	- Settings for controlling ICE candidates and createOFfer/Answer hooks FF 42
	- Remove *moz* prefix from PeerConnection FF43

## Optimizing the customer experience

Ok, the demo works. Now how do you build a reliable WebRTC service that scales? Amitha will talk about techniques for ensuring reliability when dealing with WebRTC media and how to architect scalable infrastructure from day 1.

<iframe width="560" height="315" src="https://www.youtube.com/embed/NLXWKUDPiDA" frameborder="0" allowfullscreen></iframe>

### Amitha Pulijala - Oracle

- CX vs UX (Customer experience)
- Customer expectation - Consistent video and voice
- Broken Journeys drive customers away
- Complex - multiple networks, devices and channels
- Tip 1. Enable seamless Journey (prepare for)
	- Reload
	- Back button hit
	- Native app crashes
	- IP network connectivity changes (i.e. WiFi to Mobile)
	- Device Handoffs
	- Server side failures
	- All can be solved using "Session Re-hydration"
- First call set up times matter and WebRTC takes a while
- Tip 2. Identify and solve the Weak Points
		- Identifying is the tricky part
		- Any call drop and patchy video is a big No No (for UX)
		- Use WebRTC Statistics API to measure jitter, packet loss and bandwidth
		- Instead of dropping video, decrease resolution
		- Encode multiple resolutions, to handle network switch
		- Battery power - Use Push notifications, instead of polling (drains battery)
- Success in the enterprise - Interoperability is the Key
	- IE stop gap
		- Flash fall-back solution
		- IE plugins that you can use for multiple versions of IE
		- Wait for the Edge
	- Safari
		- Native iOS webRTC support
		- People can use Chrome on Macs
	- Mobile is different
		- People don't like battery drains
		- Hardware acceleration is very important
		- Video coding with dedicated hardware - better performance and battery saving
		- Fall-back ot H.264 where VP8 (hardware acceleration) is not supported by native chip-sets
		- VP9, Daala, Thor - the war never ends
	- "Be everywhere, do everything, but never fail to astonish the customer" ~ Macy's Motto
- Q. Any expectation for customers to move from IE to Edge? A. Probably not, too committed to particular version of IE.

## Beyond P2P: Video Routing in WebRTC

Dealing with video conferences with many users, trying to setup your own Meerkat/Periscope, or just want to get WebRTC’s various codecs to work together? You’re going to need to do some media processing - Emil from Jitsi, an open source WebRTC media server, will walk you through the why & how.

*Note: I recommend watching this talk.*
<iframe width="560" height="315" src="https://www.youtube.com/embed/cmzERa0bk0Y" frameborder="0" allowfullscreen></iframe>

### Emil Ivov - Atlassian

- Why Pear to Pear (p2p) is Great
	- Better security (90% BS) :) - Unless there is a direct cable from user to user...
	- Lower Latency (50%) - Sometimes Amazon might be better
	- Less hassle (75%) - Still need servers for signaling, and turn servers in some cases.
	- Lower Cost (25%) - You pay for A LOT less Bandwidth, the one that mekes the most sense
- 3 Options
	- P2P (huge mess when a lot of endpoints involved)
	- Multipoint control unit (MCU) - Encoding/decoding very heavy, synchronization, latency unavoidable. Good for legacy
	- Selective Forwarding Unit (SFU) - 1000 videos, 550Mbits, 20% CPU
		- Simulcast - 3 video quality streams (normal, high, low) - independent streams
- Use endpoint generated Bandwidth estimation (REMB)
- How would you do it today? Only Chrome for now, but will be supported by many browsers soon.
- Q. Different codecs, in selective forwarding? A. Big problem. Multiple non optimal solutions. Everyone should support VP8 :)

## Best practices for WebRTC security

WebRTC is designed with many mandatory security mechanisms, but that doesn’t mean you don’t have to worry about security. Philipp of &yet will walk us through how to secure your WebRTC app and common exploits and caveats.

*Note: I recommend watching this talk.*
<iframe width="560" height="315" src="https://www.youtube.com/embed/Gr7PJAyMJdU" frameborder="0" allowfullscreen></iframe>

### Philipp Hancke - &yet - [webrtchacks.com/about/fippo](https://webrtchacks.com/about/fippo/)

- Facetime
	- No WebRTC
	- Years of experience
	- Use H.264, no H.265 on Wifi (better battery)
	- Uses turn servers
	- Fast turn candidate allocation, reduces call set up time
- Whats Up - Voice calls
	- NO WebRTC
	- pjsip Library
	- No Interactive Connectivity Establishment (ICE)
	- Audio Codec - OPUS Different sampling rate
	- Always relayed for the first few seconds, then switched to P2P
- Viber
	- No WebRTC
	- Not using RTP
	- All traffic encrypted
	- Can still see traffic pattern
	- Switch from relay servers to P2P
- Skype
	- Dynamically adapts sampling rate, based on network rate
	- Used turn server, which could be far from the client (Probably could be improved?)
	- Uses Opus, browser interoperability using WebRTC
	- Their own version of LibOpus
	- Lower bit rate than Chrome
	- Heavily tuned for a good Audio experience
- Facebook Messenger
	- Uses webrtc.org
	- Browser - common WebRTC usage pattern
	- Mobile - heavily tuned
	- Codecs
		- Different for different browser
- Lessons learned
	- A lot of adoption to Mobile networks
	- Audio way more important then video
	- Codec Tunning
	- ICE
		- Relay first to reduce setup time
		- Switch to p2p if successful
- Q. Most surprising finding? A. Relay service first.

## Decisions and considerations in building your WebRTC App

Designing for mixed-endpoint topologies: From connecting WebRTC to SIP or phone endpoints, to designing for hybrid mesh/SFU topologies or working across both ORTC and WebRTC until the standards align, Rob from Twilio will talk through design approach, frustrations and lessons learned in building a signaling framework and client SDKs to support it all.

*Note: I recommend watching this talk.*
<iframe width="560" height="315" src="https://www.youtube.com/embed/HJU15kH5z3k" frameborder="0" allowfullscreen></iframe>

### Rob Braizer - Twilio

- Something will break, very complex setup
- Test constantly
	- Set of End to End testers, that are continuous testing the service, like the customer will.
	- 1st approach node-webrtc, to act as a client. Difficult, server side WebRTC is not there yet.
	- Broke off signaling tests from media tests
	- Web sockets - signaling
	- robocollers (headless browsers) media tests - less often, every 5 minutes
	- Pull data into [Rollbar](https://rollbar.com/) (Error tracking tool)
	- End to end testing tools. Automated tests don't always catch everything
	- Heavy - Ready To Go -  scenarios ready to go, used to exercise specific areas.
- Recovery from failure
	- What if a load balancer goes away?
		- What would happen if all clients start hammering available load balancer?
		- Resulted in **extensive rate limiting** on load balancers and gateways
- Expect lousy networks
	- Use [Network Link Conditioner](http://nshipster.com/network-link-conditioner/) (Mac) for testing
	- Created node app that runs on raspberry pie, simulate 3g, 4g network, etc. Allows to run tests under different network conditions
- **Webrtc getSTats() API is your friend**
	- Patterns to look for
		- Packet loss
		- Spikes and Jitter
		- Calls with length of 5 sec or more, but 0 audio input - may be one-way audio
		- Look for patterns by account, enpoint Identify, browser version. (i.e. latest release of Chrome increased one-way audio)
- **Operational Excellence is a Culture Issue**
	- **Build it, operate it ( NO OPS)**
	- Regular fire drills
	- Time to recovery reports
- **Communication tools are only as good as their availability**
- Q. Most common problem? A. One way audio.
- Q. Video? A. It's all audio product (mostly) for now
- Q. What tools are you using? A. Rollbar, some internals. Key is to use getSTats. Automated selenium based tests on beta channel and Canary.

<a name="google"></a>
## Google : What's next for WebRTC?

Always the highlight of this event, Google provides the nitty gritty details on what they are doing to progress WebRTC and their internal developments to help your application succeed.

*Note: I recommend watching this talk.*
<iframe width="560" height="315" src="https://www.youtube.com/embed/HCE3S1E5UwY" frameborder="0" allowfullscreen></iframe>

### Google WebRTC Team - Serge and Justin
- Tons of stuff and only 40 minutes
- Vital Signs
	- Tracking 720 companies that use WebRTC
	- **28 WebRTC relates acquisitions this year**
	- API usage is up
- News
	- Alliance for Open media (aomedia.org)
		- Amazon, Netflix, Microsoft, Intel, Cisco, Mozilla, Google
		- TLDR: Open Codec - Lets build a standard that works
	- Microsoft supports VP9 in Edge
- Public service announcement
	- IP Addresses "Leakage"
		- P2P
			- Checks all your addresses (3G, WiFi) to find best path
			- Common expectation is that if you are using VPN everything should go through VPN (Not the case)
			- This presents a problem when users trying to hide their IP via VPN
		- TLDR:
			- Behavior was by design,
			- Can be solve, while maintaining quality
			- First step
				- Chrome extension: [WebRTC network limiter](https://chrome.google.com/webstore/detail/webrtc-network-limiter/npeicpdbkakmehahjeeohfdhnlpdklia?hl=en)
					- Follow default route, not the optimal path
			- Once issues are resolved, it will be enabled by default
				- Sites with camera permission can still get previous Behavior
				- Use the plug-in so you can provide feedback
 - **ONLY HTTPS will be allow to use "Get user media" starting December**
 - [test.webrtc.org](https://test.webrtc.org/) tool to test WebRTC components, [available on GitHub](https://github.com/webrtc/testrtc)
- If you did not report it on [webrtc.org/report-bug](http://www.webrtc.org/report-bug) it did not happen
- Already in
	- Delay Agnostic Echo Canceler
	- Faster screen sharing in Chrome 45 (Demo)
	- Mobile performance
		- 5x faster rendering
		- Battery and CPU performance
	- Improvement in video Smoothness Chrome 45 vs Chrome 46
- Around the corner *Note: A lot of stuff, watch the video*
- webRTC/ORTC Related
	- 1.0 Targeting EOY2015
		- Incorporates many ORTC objects
		- **New object provide more direct control**
			- Switch cameras/codes/tracks on the fly
			- **Set max bit rate**
			- Configure Simulcast (hopefully)
	- Whats after 1.0? WebRTC NV
		- Fully converges with ORTC
			- Apps can program to 1.0 (high level) or object API (lower level)
- Q. Are you committed to close the gap between what Hangouts can do, and what 3rd party gets. A. Everything hangouts get you get access to.
- Q. Screen sharing is enabled, is it possible to only do tab sharing? A. May be.

## The future of ORTC with WebRTC

Trent Johnsen from Hookflash will review of Object RTC (ORTC) and how its improvements are making they making their way into WebRTC already. Bernard Aboba will then discuss some ORTC-based WebRTC implementation examples, including Microsoft's new Edge browser.

<iframe width="560" height="315" src="https://www.youtube.com/embed/nQ_NgkpLyjw" frameborder="0" allowfullscreen></iframe>

### Trent Johnsen - Hookflash

- Hookflash - Founder, Chair, and Editor of ORTC Community Group
	- What is ORTC - Object Real Time Communication
		- Top 10 Benefits
			1. Mobile network hand-off
			1. Optimized for Mobile
			1. IPv6 and mobile networks
			1. SDES/SRTP transport
			1. Capabilities exchange
			1. Simulcasting / SVC
			1. Asymmetric Audio/Video (Multiple cameras, multiple microphone etc.)
			1. Media Forking
			1. Signaling flexibility - no offer/answer exchange every time a transaction takes place
			1. Direct programmer control over media pipeline
- WebRTC/ORTC road map is getting cleaner - evolution + integration

### Bernard Aboba via video (Microsoft)
- Microsoft
- WebRTC Related Blog Posts
	- [Bringing Interoperable Real-Time Communications to the Web](http://blogs.msdn.com/b/ie/archive/2014/10/27/bringing-interoperable-real-time-communications-to-the-web.aspx)
	- [Announcing media capture functionality in Microsoft Edge](https://blogs.windows.com/msedgedev/2015/05/13/announcing-media-capture-functionality-in-microsoft-edge/)
	- [Announcing VP9 support coming to Microsoft Edge](https://blogs.windows.com/msedgedev/2015/09/08/announcing-vp9-support-coming-to-microsoft-edge/)
	- [Skype for Web (Beta) Now Available Worldwide](http://blogs.skype.com/2015/06/05/skype-for-web-beta-is-now-available-to-everyone-in-the-us-and-uk/)
- [Join Windows 10 insider program to get preview builds](https://insider.windows.com/)
- [Visit https://dev.modern.ie/platform/status/ to see feature status](https://dev.modern.ie/platform/status/)

### Question to all of the vendors (Chrome, Firefox and IE Edge)
- Q. Cross browser support? A. [addaptor.js](https://github.com/webrtc/adapter) is the best bet for the near future.

## On stage: Building a WebRTC App

For our last session, we let Tim Panton loose on stage to build a WebRTC application from scratch as he details his application logic.

<iframe width="560" height="315" src="https://www.youtube.com/embed/TLXmB2TZyZE" frameborder="0" allowfullscreen></iframe>

### Tim Panton - WestHawk Consulting

- IOT Introduces a lot of security problem (i.e. Hacked Chrysler)
- Ideal protocol for IOT
	- Standard
	- Secure
	- Widely deployed
	- p2p
	- Real time
	- Strong on Identity management
	- Mobile capable
	- User-Centric
- WebRTC is ideal protocol for IOT, minus the Identity management
- Presenter:
	- Implemented Minimal webRTC signaling service in Scala [github.com/steely-glint/fingersmith](https://github.com/steely-glint/fingersmith)
	- Referenced [The Resurrecting Duckling](https://www.cl.cam.ac.uk/~fms27/papers/1999-StajanoAnd-duckling.pdf) as a good solution for Identity Management
		- TLDR; Device trusts first thing it sees - First connect claims the ownership
	- Demonstrated a (patent pending) implementation of Identity Managment for WebRTC using QR codes.
	- Did 2 demos showing his IOT in action
		- Using Tablet
		- Using hacked Lego Toy, proving that it will work even on very light resourced IOT devices
- He will be speaking again at [The IIT RTC Conference and Expo](http://www.rtc-conference.com/) if you'd like to learn more.
