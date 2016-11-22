Menu

  * [Technology](http://www.apixio.com/about/technology/)
    * [Our Platform](http://www.apixio.com/about/technology/)
  * [Solutions](http://www.apixio.com/solutions/)
    * [HCC Profiler](http://www.apixio.com/solutions/)
  * About
    * [Executive Team](http://www.apixio.com/team/)
    * [Investors &amp; Board](http://www.apixio.com/investors-board/)
    * [News Coverage](http://www.apixio.com/about/news/)
    * [Press Releases](http://www.apixio.com/press-releases/)
    * [Events](http://www.apixio.com/about/events/)
    * [Resources](http://www.apixio.com/resources/)
  * [Blog](http://www.apixio.com/blog/)
  * [Contact Us](http://www.apixio.com/contact-us/)
  * [Careers](http://www.apixio.com/join-apixio/)We’re Hiring!

** [ ![The data science company for healthcare.](http://www.apixio.com/wp-content/uploads/2015/10/apixio-logo.png) ](http://www.apixio.com/ "Apixio" ) **

#  The Apixio Engineering Blog

##  Four Key Updates from the Chrome Dev Summit

Alex Kras  |  November 21, 2016

![Rear view of man gesturing with hand while standing against defocused group
of people sitting at the chairs in front of him](http://www.apixio.com/wp-
content/uploads/2016/11/iStock-541976598-1.jpg)

Last week I attended the [Chrome Dev
Summit](https://developer.chrome.com/devsummit/),[ Google’s annual conference
on web development](https://developer.chrome.com/devsummit/). While the entire
Summit was interesting (and you can see my full notes
[here](http://www.apixio.com/technical-post/notes-from-the-2016-chrome-dev-
summit/)), I was particularly struck by a handful of updates which will have a
direct impact on Apixio’s products. I believe that other companies with web-
facing products might find those updates interesting— so I’ve listed them
below.

## Background on Apixio

Apixio is in the medical payment automation business. We use machine learning
to analyze medical records and predict what medical codes healthcare providers
can submit for payment to the Centers for Medicare and Medicaid Services. Most
of the industry is doing this process by hand. Thanks to our technology we are
able to find more billable codes (money) much faster than a medical coders
could do on their own.

Our existing users are processing large amounts of information, so they are
usually using a laptop on a fast internet connection. At the same time we are
developing new technology that will use machine learning to enable healthcare
professionals to provide better care to their patients; this will be used by a
more varied audience that won’t necessarily have access to such sophisticated
infrastructure. I believe some Web APIs announces at Chrome Dev Summit could
go a long way in helping us with that effort.

For example, let’s imagine a doctor who is walking through a hospital. She
walks into patient’s room, takes out her mobile device and tries to pull up
some patient data…

## Key Update #1: Easing Sign-In While Preserving Security

As with any medical related company, data security is our main concern. We
want to ensure that only authorized users can get access to patient’s data,
for both legal and ethical reasons

Two APIs that were announced at the Chrome Dev Summit are of particular
interest here: [Credentials
API](https://developers.google.com/web/updates/2016/04/credential-management-
api) and [Face Recognition API](https://www.microsoft.com/cognitive-
services/en-us/face-api/documentation/overview).

Credentials API will allow the browser to keep track of sites that a user has
already authenticated with, allowing users to access sites from various
devices without having to re-login. In our hypothetical example the mobile
browser would know that the doctor already signed-in to Apixio on her computer
and would allow her to access the patient data on her phone without re-
authenticating

We will be able to use Face Recognition API to confirm that the person trying
to access the data is our doctor and to prevent other people from getting
access to this sensitive information.

## **Key Update #2: More User-Friendly App Installation and Update**

Assuming the doctor is on an Android device, she will be able to easily add
our web app to her home screen, making it appear identical to a native app.
Chrome on Android will detect if user has visited a site multiple times and
(assuming our site has a [web manifest](https://developer.mozilla.org/en-
US/docs/Web/Manifest) file in place) will prompt the doctor to add our site to
her home screen. Alternatively, she will be able to add the application
manually via an option in the Chrome menu.

For us as a business, using a web app means no long waits for the App Store
approval and no need for expensive marketing to get users to download our
native app. If they visit our site a few times, they will be prompted to add
it to their home screen.

Equally important, there is no longer need to wait for App Store approval
every time we want to update the app. All we have to do is update the [Service
Worker](https://developer.mozilla.org/en-US/docs/Web/API/Service_Worker_API)
version (a variable in our source files), which will initiate an update of our
app next time the user connects to the internet.

## **Key Update #3: Offline Support**

I am sure that internet connection can be spotty in most hospitals. Currently
our app would be of little use, if the doctor was offline.

Thankfully with the [Service Worker API](https://developer.mozilla.org/en-
US/docs/Web/API/Service_Worker_API) this is no longer an issue. Service Worker
allows us to cache the app files as well as the needed patient information on
a doctor’s phone. That way, even if she were to open our app in Airplane Mode,
we would still be able to render it properly.

What would happen if the doctor were to take some notes while her phone was
offline? Service Worker will work in combination with [Background Sync
API](https://developers.google.com/web/updates/2015/12/background-sync) to
save the data on her phone and send it to our server once the doctor goes back
online.

## **Key Update #4: Push Notification**

Let’s assume while our doctor is conducting rounds, our machine learning
algorithm identifies a certain patient who could be at high risk for a
heretofore unnoticed condition. With the help of Service Worker and [Push
Notification API](https://developer.mozilla.org/en-US/docs/Web/API/Push_API)
we’ll be able to easily notify the doctor about the new development, giving
her the information when she needs it the most.

## **This is Only the Beginning**

I think these examples are barely scratching the surface of what is possible.
New Web Standard are helping to push the Web forward. We are witnessing the
Mobile revolution similar to the Desktop revolution of early 2000s, when all
software made it’s way to the cloud.

Take a look at my [notes from Chrome Dev
Summit](http://www.apixio.com/technical-post/notes-from-the-2016-chrome-dev-
summit/), if you would like to learn more about various APIs and tools
discussed at the summit that were not mentioned in here.

Please consider visiting our [careers page](https://appirio.com/careers), if
you can see yourself working on some of the ideas described in this post.

hidden

![apixio blog](http://www.apixio.com/wp-content/themes/apixio-
theme/images/apixio-blog-logo.png)

success!

Thank you for subscribing to our blog.

![Sending ...](http://www.apixio.com/wp-content/plugins/contact-
form-7/images/ajax-loader.gif)

Error: All input fields are required!

SUCCESS!  
Thank you for subscribing to our blog.

####  TECHNOLOGY

  * [Our Platform](http://www.apixio.com/about/technology/)
  * [HCC Profiler](http://www.apixio.com/solutions/)
  * [Engineering Blog](http://www.apixio.com/engineering-blog/)

####  RESOURCES

  * [Blog](http://www.apixio.com/blog/)
  * [Case Studies](http://www.apixio.com/resources/)
  * [White Papers](http://www.apixio.com/resources/)

####  ABOUT US

  * [Team](http://www.apixio.com/team/)
  * [Investors](http://www.apixio.com/investors-board/)
  * [Media](http://www.apixio.com/about/news/)
  * [Events](http://www.apixio.com/about/events/)

#### Add

  * [Careers](http://www.apixio.com/join-apixio/)We’re Hiring!

* [Terms of Use](http://www.apixio.com/terms-of-use/)
* [Privacy Policy](http://www.apixio.com/privacy-policy/)
* [Contact Us](http://www.apixio.com/contact-us/)

#### Request a demo

Success!  
We'll be in touch with your shortly.

Error: All input fields are required!

SUBMIT ![Sending ...](http://www.apixio.com/wp-content/plugins/contact-
form-7/images/ajax-loader.gif)

[ ![](http://www.apixio.com/wp-content/uploads/2016/07/footer-logo.png)
](http://www.apixio.com)

Apixio © 2016. All rights reserved.

  * [Facebook](https://www.facebook.com/Apixio-141522885871911/?fref=ts)
  * [Twitter](https://twitter.com/Apixio)
  * [LinkedIn](https://www.linkedin.com/company/apixio)


