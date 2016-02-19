I love [Meld](http://meldmerge.org/). It's is my favorite diff tool, and one of the tools I missed the most when I switched over to Mac from Linux.

<a href="http://www.alexkras.com/wp-content/uploads/meld.png"><img src="http://www.alexkras.com/wp-content/uploads/meld-300x81.png" alt="meld" width="300" height="81" class="alignright size-medium wp-image-648" /></a>

Except, you can run Meld on Mac too. The easiest way is using [Homebrew](http://brew.sh/), via `brew install meld`. If you don't have Homebrew on your Mac yet, [it will only take a minute to install](http://brew.sh/) via one simple command, and you will probably end up installing it at some point anyway.

<p class="note">
Note: `brew install meld` will probably fail, but the error will show you the proper command to run. In February of 2016 for me that command was `brew install homebrew/gui/meld`, some people report that `brew install homebrew/x11/meld` worked for them. Just read the outputted message carefully. It will probably have to pull in a lot of dependencies so it might take a while, but it should work.
</p>

For some reason Homebrew did not work for me on my new Mac back in February of 2015, so I had to look for other options (hence the "Without Homebrew, MacPorts, or Think" part in the original title of this article).

After some intense Googling, I came across this [AWESOME fork of Meld](https://github.com/yousseb/meld/releases/tag/osx-v1). It is Meld packaged with all of the dependencies into a regular **.dmg**. You can download it, install it, and it just works.

<p class="note">
Note: I am linking to release tagged osx-v1, there have been other releases since then. Some of them did not work for all users, but the latest release suppose to fix that. You might have to try a few release to find the one that works for you. The author of of that package posts his updates in the comments sometimes, so be on a lookout for that. If all fails I recommend using version osx-v1, since it seems to work for most users.
</p>

As I said earlier, Meld.dmg "just worked" for me, except that it didn't work in the command line, and that is where I need it the most.

I wrote the following script (in python since you already need it to run meld) and placed it in `~/bin` folder (making sure to add ~/bin to my PATH, see bellow).

<p class="note">
Note: There is a cleaner version posted in the comments that should work with 3 arguments, allowing you to use meld as a merge tool. I have not tested it, but it looks like it should work, and it might be worth your time to try it first.
</p>

<pre>
#!/usr/bin/python

import sys
import os
import subprocess

if len(sys.argv) > 1:
  left = os.path.abspath(sys.argv[1]);
else:
  left = ""

if len(sys.argv) > 2:
  right = os.path.abspath(sys.argv[2]);
else:
  right = ""

MELDPATH = "/Applications/Meld.app"

p = subprocess.call(['open', '-W', '-a',  MELDPATH, '--args', left, right])
</pre>

I then added that folder to my PATH via `export PATH=~/bin:$PATH` entry in my `.bashrc` file, to make sure that meld command got picked up in my terminal. You can reload your bash config via `. ~/.bashrc` or just restart the terminal. Type in `meld` and it should work.

I've been using it for a <strike>few weeks</strike> many months now, and yet to run into any problems. So there you have it, a working Meld on Mac OS X Yosemite, without having to use any 3rd party tools.

- **Updated February 13, 2016**
    - Updated homebrew instructions
    - Updated Meld fork reference instructions
