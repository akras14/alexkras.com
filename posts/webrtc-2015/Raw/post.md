# Kranky Geek 2015 - WebRTC conference
http://www.krankygeek.com/

## Brief Welcome
<iframe width="560" height="315" src="https://www.youtube.com/embed/Zl650wbirYE" frameborder="0" allowfullscreen></iframe>

### Tsahi Levi-Levent - bloggeek.me
- WebRTC easy vs VOIP, nothing beats that.
- Continuous slow growth, not exponential.
<!-- {{Slide of questions vs answers webRTC}} -  -->


## A closer look at the WebRTC UX/UI API

User interaction for real time communications is way different than dealing with typical web content and streaming media. Arin will cover best practices for incorporating WebRTC into your application for a smooth user experience.

*Note: I recommend watching this talk.*
<iframe width="560" height="315" src="https://www.youtube.com/embed/H7hAapxpsOY" frameborder="0" allowfullscreen></iframe>

### Arin Sime - webrtc ventures (Real time Weekly)

- Technology is cool, but users don't care. (Metaphors like Skype in your browser)
- All users care about is experience
- Allow/Block - what do you do if they block?
- How do you warn them, that you about to share their camera, even if they already gave the permission earlier (like a month ago).
- UX Terms
  - Micro Interactions (minor things that users don't notice, but that make big difference)
  - Information Hierarchy (Structure and placement - symbolize importance)
  - Feedback (Feedback to the user, making it obvious what is going on)
- To show or not to show it's own camera
- Larger controls for mobile apps
- Use overlays wisely, and temporarily
- Multi-party - performance - put their picture if camera is paused, so you know who is speaking
- Provide feedback before and during on status of connection
	- (i.e. warn if conneciton is really slow,
	- mediocore connection - warn them that the video will be paused.)
	- Connection goes bad, you can pause the video, and still keep the audio
	- Testing the code quality
- Maintain focus, emphasize what important but keep the other stuff in
- Everything matters even more with mobile
- Key point - Much more than a video tag

## Application Chats

Hear first hand the choices & decisions an app dev faced with their WebRTC app, how they made them, what they did and what would they recommend you consider. Great quick speakers from Freshdesk, Wix.com and Skedans.


### Skedans

<iframe width="560" height="315" src="https://www.youtube.com/embed/7_34WfyOjx4" frameborder="0" allowfullscreen></iframe>

- Value - more than just browser to browser communication without plugin
- Very easy to set up real time app in peer to peer mode
  - But more than 4,5 parties need centeralized server
  - Skedans - platform RTC
  - Drone + webRTC example (flight and control)

### FreshDesk

*Note: I recommend watching this talk.*
<iframe width="560" height="315" src="https://www.youtube.com/embed/d1KBSTaxmtE" frameborder="0" allowfullscreen></iframe>

- Why WebRTC is part of it (Cloud based customer support software)
- SF, 50,000 customers - democratize customer support - make it available to everybody
- Leads to technology choices to facilitate that.
- Support
- Voice 80% (phone)
  - You want to provide prestine experience
  - How do you make sure this is available without clunky instalations
  - That is where WebRTC comes to play
  - Customers got to:
    - Log in
    - Configure
    - Ready to go - No implemenations requeired
    - Uses Twillio WebRTC solution
- Chat
- Video
- WebRTC both powerful and versitile
- Click to call - one way feature
- Throw some JS on page and immediately customers can interact with agents
- Allows for superb user experience
- Translate complicate technology into easy to use interface
- Q. How do you deal with browsers that don't support
A. Fall back to flash (which is not desirable)
- Q. Infrastructure
A. Voice, email, chat - centrilize using Twillion API

*Note: I recommend watching this talk.*
### Wix.com - Build websites

<iframe width="560" height="315" src="https://www.youtube.com/embed/FV9VA4JhZjQ" frameborder="0" allowfullscreen></iframe>

- Wix.com needs a lot of customer support
- Flash was problematic
- 2 types of users
  - Support Agents
  - Person building their site
- Use Twillio
  - They offered WebRTC and they jumped on it
  - Instant user feedback
  - Nice open platform (Chrome/Firefox)
  - Users can schedule a call and will be in
  - Twillio allows to build custom call center solution
    - Python API
    - Alerts
    - Downtime
    - Custom Routing
    - Really easy to set up, no need to dig into internals (just voice for now)
    - Looking into customizing for screen sharing
    - No plugins to monitor, just keep Chrome up to date
    - Open socket to Twillio
    - Another socket to update all updates inside Call Center Application
    - Very easy to roll back to Flash
- Differetn in Chrome vs FF, test
- Flash is removed on Mobile, but WebRTC supported on Androind
- Bridge from Phone line (outside) bridge to their WebRTC app (Worsk really well for them)
Using Twillio API

## IBM Bluemix: Mixing voice & data

*No video available (yet?)*

In this demo, a video call (using the new Twilio video API) is held between a customer and a customer service agent. As the video call is happening IBM Watson Speech to Text service is transcribing the audio in real time. After the video call completes, Alchemy API is used to automatically determine which product the customer was giving feedback on and then determines the sentiment of that feedback. The corresponding product's feedback score, a number between 0 and 100, fluctuates based on this feedback. After the score is updated, Business Rules are invoked to determine if the product has crossed a threshold to automatically suggest a review of investment in the product. If the rules suggest a review, a process instance for a change in product investment is then started and managed by the Bluemix Workflow service. This creates a task for a buyer at the company. The buyer can then decide whether to ignore or go through with the review, thus completing the process.

### Jeff Sloyer - IBM Bluemix

- WebRTC invaded the Doctors Office
- Demo (Node app)
   - Real time transcribing using Watson
- Bluemix - hosting with Watson access
- Built in 3 days
   - WebRTC + BlueMix (and Twillio?) makes your life as a developer really easy
- A lot of stuff not documented well
- Convert WebRTC to Watson supported audio file
- Send it to node backend
- There is NPM package for Watson
- Challenges
  - Order to start a call had to be started by a doctor for some reason
  - Issue for remote streams in Chrome vs FF
  - Multiple wesocket audio streams are hard
  - Getting the audio format right (Watsons docs didn't mentioned supported format at the time)
  - Personality of the patient (can't figure out until the call is over...)
  - Scalling websockets
  - Spying on the media stream (is hard and not well documented)
  - Websocket to Watson droped a lot, wrote re-try logic
- Questions
  - Is this live? Twillion-vidoe.mybloomex.net - Patient can only be in a web browser
  - Hippa complience. BlueMix is complient, encrypted, and spent a lot of time on that.

## What is Mozilla doing with Firefox?


*Note: I recommend watching this talk.*
<iframe width="560" height="315" src="https://www.youtube.com/embed/WZhqWvFHGSo" frameborder="0" allowfullscreen></iframe>

WebRTC allows the sharing of screen content - Mozilla has some cool demos to share which highlight the power of WebRTC beyond the typical voice/video communications that we typically think of. Plus, we'll get an update on the continued progress of Firefox with WebRTC.

### Nils Ohlmeier - Mozilla

- Canvas
  - Firefox allows using canvas as an input for youre PeerConnection (take canvas instead of camera)
  - Available in FF 41
  - Expected to be live in FF 43
  - Replace Camera with Canvas as video input
  - Can do Camera to Canvas -> Do some magic on Canvas -> Stream to WebRTC
  - Links in Screenshots
  - Gets more interesting
    - Multiple cameras to one Canvas and stream that
    - Can do a MCU
- IPv6 support FF 42
- Support ICE TCP FF 42  (preffed off, on in FF43-44)
- Upcoming Audio Features
  - Audio perf improvements (esp on Windows)
  - Support for strereo sound
  - Up 16 to 32 KHz Audio
  - !! Audio capture for screen sharing (FF43)
- More
  - Simulcast support
  - applyConstraind for gUM Media stream  !! Make lower resolution !! FF43-4
  - Prefs for cotnrolling ICE candidates and createOFfer/Anser hooks FF42
  - Remove moz prefix from PeerConnection FF43
- Questions
  - Canvas to standard - Based on the draft, potentially API could change, but it's a small API
  - Video mixing(canvas) what is the performance - Not sure, there is perf diff, MCU demo was limited to 8 for example. Probably don't want to use it for your professional video mixing. Double check it on your machine.

## Optimizing the customer experience

<iframe width="560" height="315" src="https://www.youtube.com/embed/NLXWKUDPiDA" frameborder="0" allowfullscreen></iframe>

Ok, the demo works. Now how do you build a reliable WebRTC service that scales? Amitha will talk about techniques for ensuring reliability when dealing with WebRTC media and how to architect scalable infrastructure from day 1.

### Amitha Pulijala - Oracle

- CX vs UX (Customer experience)
- Expected
  - Consistend video and voice
- Brokek Journeys drive customers away
  - Complex
    - Multiple netowrks, devices and channels
- Tip 1. Enable seamless Journey
  - Reload
  - Back button
  - Native app crashes
  - IP networ connectivit changes - WiFi - 4g
  - Device Handoffs
  - Server side failures
  - Can be solved using "Session Rehydration" (Separate slide with a lot of text)
- Dymanic Media Peering
  - First call set up times matter
  - WebRTC takes a while
  - Can be resolved
    - Dynamic Mdeia Peering
      - Prioritoize the cnadidate ata are most liketly to work first
      - ...
- Tip 2. Identify and solve the Weak Points
    - Identify is tricky
    - Call drop more and Patchy video a No No
      - Use WebRTC stats API to measure
        - Jitter
        - Packet loss
        - Bandwidth
      - Can drop video, decrease resolution
      - Encode multipe resolution, to handle network Switch
    - Battery power
      - Use Push notifications, instead of polling (drains battery)
      - Mobile and Chrome
- Inter operability is the Key to success in the enterprise
  - IE stop gap
    - Flash fallback solution (Customers look funny at that)
    - IE plugins that you can use for multiple versions of IE
    - Wait for Edge
  - Safari
    - Native iOS webRTC support
    - People can use Chrome on Macs
  - Mobile is different
    - Don't like battery drains
    - Hardware acceleration is very important
    - Video coding with dedicated hardware - better performance and battery saving
    - Fallback ot H.264 where VP8 (hardware acceleration) is not supported by native chip sets
    - VP9, Daala, Thor - the war never ends
  - "Be everywhere, do everything, but never fail to astonish the customer"
- Q. Any expectation for customers to move from IE to Edge. A. Probably not, to commited to particular version of IE.
- Demo: shoutcloud.us.oracle.com:7002
  - Simple video sharing with Auth, Video and Chat
   - Re-load
    - Video, Audio, Data, chat gets re-established

## Beyond P2P: Video Routing in WebRTC

Dealing with video conferences with many users, trying to setup your own Meerkat/Periscope, or just want to get WebRTC’s various codecs to work together? You’re going to need to do some media processing - Emil from Jitsi, an open source WebRTC media server, will walk you through the why & how.

*Note: I recommend watching this talk.*
<iframe width="560" height="315" src="https://www.youtube.com/embed/cmzERa0bk0Y" frameborder="0" allowfullscreen></iframe>

### Emil Ivov - Atlassian

- Why P2P
  - Better securit (90%BS) :) - Unless there is a direct cable from user to user...
  - Lower Latency (50%) - Sometimes Amazon might be better
  - Less hassle (75%) - Still need servers for signaling, and turn servers in some cases.
  - Lower Cost (25%) - You pay for A LOT less Bandwidth, the one that mekes the most sense
- Slide with options
  - P2P mess (a lot of endpoints)
  - MCU - Encoding/decoding very heavy, synchronization, latency unavoidable. Good for lagacy
  - SFU - 1000 videos, 550Mbits, 20% CPU
    - What about Mobile, there is a work around
    - Simulcast - 3 video quality streams (normal, high, low) - independent streams
    - Other options (Scalable Video Coding(SVC) - Crappy version to good version, like Image loading)
    - Temporal SVC - Similar to ^ but difference in Frame rate vs
  - Use endpoint generated Bandwidth estimation (REMB)
  - How would you do it today? Only Chrome for now, but will be supported by many browsers soon.
  - Q. Forwarding units? A. Development work, yes, processing work, none.
  - Q. Different codecs, in selective forwarding. A. Big problem. Multple not option solutions, don't implemente it in your fowarding unit. Everyone should support VP8 :)

## Best practices for WebRTC security

WebRTC is designed with many mandatory security mechanisms, but that doesn’t mean you don’t have to worry about security. Philipp of &yet will walk us through how to secure your WebRTC app and common exploits and caveats.

*Note: I recommend watching this talk.*
<iframe width="560" height="315" src="https://www.youtube.com/embed/Gr7PJAyMJdU" frameborder="0" allowfullscreen></iframe>

### Philipp Hancke - &yet

- Security
  - Tooling
    - Wireshark
      - Not good at visualizing things
    - Generatd charts with highCharts
    - Vrote using something else...
  - Apps
    - Facetime
      - Not using WebRTC
      - Rumored to be big
      - Years of experience
      - Use H.264, no H.265 on Wifi (better battery)
      - Uses turn servers
      - Fast turn candidate allocation, reduces call set up time
    - Whats Up - Voice calls
      - NOo webrtc
      - pjsip Library
      - No ICE
      - Audio Codec - opos Different sampling rate
      - Always relayed for the first few seconds, the switch to P2P
    - Viber
      - No WebRTC
      - Not using RTP
      - All traffic encrypted
      - Can still see traffic pattern
      - Switch from relay servers to P2P
    - Skype
      - Dynamically adapts sampling rate, based on network rate
      - Used turn server, somewhere far from Europe
      - Uses Opus, browser interop using WebRTC
      - Their own verison of LibOpus
      - Lower bit rate than Chrome
      - Heavily tuned for a good Audio experience
    - Facebook Managers
      - Uses webrtc.org
        - Browser - common usage
        - Mobile - heavily tuned
        - Codecs
          - Different for diff browser
        - Encryption
          - ...
  - Lessons learned
    - A lot of addoption to Mobile networks
    - Audio way more important then video
    - Encryption on heavy loss ...
    - Codec Tunning
      - Diff Codecs
      - Lower bit rate
      ...
    - ICE
      - Relay first to reduce setup time
      - Switch to p2p if succesful
    - webrtchacks.com/about/fippo
  - Q. Most surprising. A. Relay service first.

<!--
## Utilizing the WebRTC Data Channel
2:45
UPDATE: Due to foreseen schedule changes, this speaker will not be joining today, we will adjust the schedule accordingly.

Feross Aboukhadijeh - webtorrent.io -->

## Decisions and considerations in building your WebRTC app

Designing for mixed-endpoint topologies: From connecting WebRTC to SIP or phone endpoints, to designing for hybrid mesh/SFU topologies or working across both ORTC and WebRTC until the standards align, Rob from Twilio will talk through design approach, frustrations and lessons learned in building a signaling framework and client SDKs to support it all.

*Note: I recommend watching this talk.*
<iframe width="560" height="315" src="https://www.youtube.com/embed/HJU15kH5z3k" frameborder="0" allowfullscreen></iframe>

### Rob Braizer - Twilio

- Something will break, very complex (screenshot)
- Test constantly
  - Set of End to End testers. That are continuolsy testing the service, like the customer will.
  - 1st approach node-webrtc, to act as a client . Difficult, server side WebRTC is not there yet.
  - Broke off signaling tests from media tests
  - Web sockets - signaling
  - robocollers (headless browsers) media tests - less often, every 5 minutes
  - Pull data into Rollbar <- Tool
  - End to end testing tools. Automated tests don't always catch everything
  - Heavy ready to go scenarios ready to go, to test specific areas.
  - Layered approach (screenshot)
- Recovery from failure
  - Screenshot
  - What if a load balancer goes away?
    - All clients start hammering available load balancer, what would happend?
    - Resulted in extensive rate limiting on load balancers and gateways
    - Make sure your Registrar can support all those writes
- Expect lousy networks
  - Network Link Conditioner (Mac) for testing
  - Create node app - networkThrottler, runs on rasbery pie, simulate 3g, 4g network, etc. Allows to run tests under different network conditions !!
- Webrtc getSTats() API is your friend !!
  - Pipe data to Amazon (Screenshots) reports on stats
  - Patterns to look for
    - Packet loss
    - Spikes and Jitter
    - Calls with 5 sec, but 0 audio input - one-way audio
    - ... Look for patterns by account, enpoint Identify, browser version. (i.e. latest release of chrome increase one-way audio)
- Operational Excelense is a Culture Issue !!
  - Write service level first
  - Build it, operate it ( NO OPS)
  - Five Whys Analysis
  - Regular fire drills
  - Runbooks
  - Post motrem
  - Time to recovery reports
- Communication tools are only as good as their availability
- Q. Most common problem. A. One way audio
- Q. Best practise injecting media streams for testing? A. Not yet, some thing...
- Q. Video? A. It's all audio product (mostly) for now
- Q. What tools are you using? A. Rollbar, some internals. Key is to use getSTats, automated tests, selenium based on beta channel and Canary.

## Google : What's next for WebRTC?

Always the highlight of this event, Google provides the nitty gritty details on what they are doing to progress WebRTC and their internal developments to help your application succeed.

*Note: I recommend watching this talk.*
<iframe width="560" height="315" src="https://www.youtube.com/embed/HCE3S1E5UwY" frameborder="0" allowfullscreen></iframe>

### Google WebRTC Team

Serge and Justin (from last year)
- Tons of stuff, and only 40 minutes
- Vital Signs
  - Tracking 720 companies ...
  - Many major use webrtc, check webrtchacks
  - 28 web rtc relates acquisitions this year !!!
  - API usage is up
- News
  - Alliance for Open media
    - Amazon, Netflix, Microsoft, INtel, Cisco, Mozilla, Google aomedia.org
    - TLDR: Open Codec - Lets build a standard that works
    - Microsoft supports VP9 in Edge
    - Apple dropping HEVC ?
- Public service announcment
  - IP Addresses "Leakage"
    - P2P
    - Checks all your addresses (3g, wi-fi) to find best path.
    - Expect if using VPN everything shoudl go through VPN (Not the case)
    - This presents a problem when users trying to hide their IP via VPN
    - TLDR:
      - Behavior was by design,
      - Can be solve, while maintaing quality
      - First step
        - Chrome extension: WebRTC network limiter
          - Follow defualt? route, not optimal path
      - Once issues are resolved, it will be enabled by default
        - Sites with camera permission can still get previous Behavior
        - Don't want to get a case where apps that don't use Camera, would ask for it, just so they can get the routing behaviour
        - Use the plugin to get/provide feedback
 - ONLY HTTPS will be allow to use "Get user media" starting December !!!!
 - Missed new audio alg???
 - test.webrtc.org OS tool that tests on github
  - Network test
  - Mic
  - etc.
- If you did not report it on webrtc.org/report-bug it did not happen
- Already in
  - Delay Agnostic Echo Canceler
  - Faster screen sharing in Chrome 45 (Demo)
  - Mobile performance
    - 5x faster rendering
    - Battery and CPU performance
  - If using webrtc.org code, you get it for free (with a flag?)
  - Improvement in video Smoothness Chrome 45 vs Chrome 46 (cool demo)
  - Event driven datachannel buffing ? (and few more ?)
- Around the corner
  - iOS API revamp
  - v2 API under way
    - Will support V2 side by side with current (for some period)
  - VP9
    - 40% fewer bits, fo 40% higher quality (up to you)
  - H.264 in Chomre
  - MediaStreamRecorder - Top Request
    - Initial focus on local MediaStreams ?
    - Goal to have behind flag in Chrome 47
    - crbug.com/262211
- Not todo yet
  - Few other
  - WebRTC in Chrome for iOS $10K bounty on a bug
- webRTC/ORTC
  - 1.0 Targeting EOY2015
    - Incorporates many ORTC objects
    - New object provide more direct controll !!
      - Switch cameras/codes/tracks on the fly
      - Set max bitrate !!
      - Configure Simulcast (hopefully)
  - After 1.0? WebRTC NV
    - Fully converges with ORTC
      - Apps can program to 1.0 (high level) or object API (lower level)
        - Complete bypass of SDP, if desired?
- Q. Bit rate Improvement on mobile. A. On Wifi came a long way...
- Q. BlueJeans in prodcution, are you commited between what Hangouts do, and what 3rd party gets. A. Everything hangouts get you get access to, ... except screen sharing.
- Q. Screen sharing, anything on tab sharing? A. May be
- Q. Mobile libs? Good way to get the stable version? A. Go to the release branch...

## The future of ORTC with WebRTC

Trent Johnsen from Hookflash will review of Object RTC (ORTC) and how its improvements are making they making their way into WebRTC already. Bernard Aboba will then discuss some ORTC-based WebRTC implementation examples, including Microsoft's new Edge browser.

<iframe width="560" height="315" src="https://www.youtube.com/embed/nQ_NgkpLyjw" frameborder="0" allowfullscreen></iframe>

### Trent Johnsen - Hookflash

- Hookflash - Founder, Chair, and Editor of ORTC Community Group
  - Tech focus - ORTC and WebRC
  - What is ORTC?
    - Object Real Time Communication
      - Top 10 Benefits
        1. Mobile network handoff
        1. Optimized for Mobile
        1. IPv6 and mobile networks
        4. SDES/SRTP transport
        1. Capabilites exchange
        1. Simulcasting / SVC
        1. Asymmetic Audio/Video - Multi cameras, multip mics, vs one to one
        1. Media Forking - Use same set of ports.
        1. Signaling flexibility - no offer/answer exchange every time a transaction takes place
        1. Direct programmer control over media pipeline
  - WebRTC/ORTC road map is getting cleaner - evolution + integration

### Bernard Aboba via video (Microsoft)
- Microsoft
  - dev.modern.ie/patform/status
    - Supported - on Edge Win 10
    - Run down on some features in the pipeline
  - Skype for web, blogpost (a while back) currently a plug in, but will be moving to native
  - Screenshot with links
  - Q. Timeframe for H.264, hardware acceleration? A. Planned, but no timelines yet.
  - Q. WebRTC timeline. A. Should not be a long wait.


Q. Cross browser support for addaptor.js.
A. Addoptor is a good way to get consistent beheaviour, for the near future, hopefully it will work for edge just as well. - Justin
A. Probably stuck with adopter.js for a long time with ORTC in the mix, but it is the best way to make progress- FF guy.
A. Not sure, about Microsoft guy.

## On stage: Building a WebRTC App

For our last session, we let Tim Panton loose on stage to build a WebRTC application from scratch as he details his application logic.

*No video available*

### Tim Panton - WestHawk Consulting

Demo

- Examples of security breaches
  - Hack Crysler
  - Hack eye sights
  - Hack Drone other drones
  - FDA - pump over WIFI
- Ideal protocol for IOT
    - Standard, secure, Widley deployed, P2p, Realtime, Strong on Identity managment, Mobile capable, User-Centric
    - Pretty much WebRTC, minus the Identity managment
- Demo - build something
  - Realtime
  - Authenticated
  - p2p
  - small Device + webRTC browser
- Compontents
  - Chrome
  - Github stelly- (screenshot)
  - Duckling protocol (screenshot)
- QR Code Exchange. First to connect - owns the connection.
- Which address token?
  -
