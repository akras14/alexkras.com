## Table of Contents

- [Introduction](#intro)
- [Minimal Theory](#min-theory)
- [Step 1. Reproduce and confirm the problem](#reproduce)
- [Step 2. Take at least 3 Heap dumps](#heapdump)
- [Step 3. Find the problem](#find-problem)
- [Step 4. Confirm that the issue is resolved](#confirm)
- [Links to some other resources](#links)
- [Summary](#summary)

<a name="intro"></a>
## Introduction

Few months ago I had to debug a memory leak in Node.js. I found a good number of articles dedicated to the subject, but even after carefully reading some of them, I was still pretty confused on what exactly I should do to debug our memory leak.

My intent for this post is to be a simple guide for debugging a memory leak in Node. I will outline a single easy to follow approach, that should (in my opinion) be a starting point for any memory leak debugging in Node. For some cases this approach may not be enough, and I will link to some other resources that you may want to consider.

<a name="min-theory"></a>
## Minimal Theory
JavaScript is a garbage collected language. Therefore, all memory used by a Node process is being automatically allocated and de-allocated by the V8 JavaScript engine.

How does V8 know when to de-allocated the memory? V8 Keeps a graph of all variables in the program, starting from a root node. There are 4 types of data types in JavaScript: Boolean, String, Number, and Object. First 3 are simple types, and they can only hold on to the data that is assigned to them (i.e. string of text). Objects, and everything else in JavaScript is an object (i.e. Arrays are Objects), can keep references (pointers) to other objects.

{image-of-data-graph}

Periodically V8 will walk through the Memory Graph, trying to identify groups of data that can no longer be reached from the root node. If it's is not reachable from the root node, V8 assumes that the data is no longer used and releases the memory. This process is called Garbage Collection.

### When does a memory leak occur?

Memory leak occurs in JavaScript when some no longer needed data is still reachable from the root node. V8 will assume that the data is still being used and will not release the memory. **In order to debug a memory leak we need to locate the data that is being kept by mistake, and make sure V8 is able to clean it up.**

It's also important to note that Garbage Collection does not run at all times. Normally V8 can trigger garbage collection when it deems appropriate. For example it could run a Garbage Collection periodically, or it could trigger an out of turn Garbage Collection if it senses that the amount of free memory is getting low. Node has a limited number for memory available to each process, so V8 has to use whatever it has wisely.

{node-error}

The later case of out of turn Garbage Collection could be a source of significant performance degradation.

Imagine you have an app with a lot of memory leaks. Soon, Node process will begin to run out of memory, which would cause V8 to trigger an out of turn Garbage Collection. But since, most of the data can still be reach from the root node, very little of it will get cleaned up, keeping most of it in place.

Sooner than later, Node process would run out of memory again, triggering another Garbage Collection. Before you know it, you app goes into a constant Garbage Collection cycle, just to try keeping the process functioning. Since V8 spends most of the time handling Garbage Collection, very little resources are left to run the actual program.

<a name="reproduce"></a>
## Step 1. Reproduce and confirm the problem

As I've indicated earlier, V8 JavaScript engine has a complicated logic that it uses to determine when Garbage Collection should run. What it means in practical terms, that even though we can see a memory for the process continue to go up, **we cannot be certain that we are witnessing a memory leak, until we know that Garbage Collection has ran**, allowing unused memory to be cleaned up.

Thankfully, Node allows us to manually trigger Garbage Collection, and it is the first thing that we should do when trying confirm a memory leak. This can be accomplished by running Node with `--expose-gc` flag (i.e. `node --expose-gc index.js`). Once node is running in that mode, you can programmatically trigger a Garbage Collection at any time by calling `global.gc()` from your program.

You can also check the amount of memory used by your process by calling `process.memoryUsage().heapUsed`.

By manually triggering garbage collection and checking the heap used, you can determine if you in fact observing a memory leak in your program.

### Sample program
I've create a simple memory leak program, that you can see here: https://github.com/akras14/memory-leak-example

You can clone it, run `npm install` and then run `node --expose-gc index.js` to see it in action.

```JavaScript
"use strict";
require('heapdump');

var leakyData = [];
var nonLeakyData = [];

class SimpleClass {
  constructor(text){
    this.text = text;
  }
}

function cleanUpData(dataStore, randomObject){
  var objectIndex = dataStore.indexOf(randomObject);
  dataStore.splice(objectIndex, 1);
}

function getAndStoreRandomData(){
  var randomData = Math.random().toString();
  var randomObject = new SimpleClass(randomData);

  leakyData.push(randomObject);
  nonLeakyData.push(randomObject);

  // cleanUpData(leakyData, randomObject); //<-- Forgot to clean up
  cleanUpData(nonLeakyData, randomObject);
}

function generateHeapDumpAndStats(){
  //1. Force garbage collection every time this function is called
  try {
    global.gc();
  } catch (e) {
    console.log("You must run program with 'node --expose-gc index.js' or 'npm start'");
    process.exit();
  }

  //2. Output Heap stats
  var heapUsed = process.memoryUsage().heapUsed;
  console.log("Program is using " + heapUsed + " bytes of Heap.")

  //3. Get Heap dump
  process.kill(process.pid, 'SIGUSR2');
}

//Kick off the program
setInterval(getAndStoreRandomData, 5); //Add random data every 5 milliseconds
setInterval(generateHeapDumpAndStats, 2000); //Do garbage collection and heap dump every 2 seconds
```


The program will:

1. Generate a random object every 5 milliseconds and store it in 2 arrays, one called _leakyData_ and another _nonLeakyData_. We will clean up the nonLeakyData array every 5 milliseconds, but we'll **"forget"** to clean up the leakyData array.
2. Every 2 seconds the program will output the amount of memory used (and generate a heap dump, but we'll talk more about than in the next section).

If you run the program, you'll see it begin to output the stats data. Let it run for a minute or two.

You'll see that the memory is quickly growing, even though we are triggering Garbage Collection every 2 seconds right before we get the stats via:

```JavaScript
//1. Force garbage collection every time this function is called
try {
  global.gc();
} catch (e) {
  console.log("You must run program with 'node --expose-gc index.js' or 'npm start'");
  process.exit();
}

//2. Output Heap stats
var heapUsed = process.memoryUsage().heapUsed;
console.log("Program is using " + heapUsed + " bytes of Heap.")
```

with the output looking something like the following:

```
Program is using 3783656 bytes of Heap.
Program is using 3919520 bytes of Heap.
Program is using 3849976 bytes of Heap.
Program is using 3881480 bytes of Heap.
Program is using 3907608 bytes of Heap.
Program is using 3941752 bytes of Heap.
Program is using 3968136 bytes of Heap.
Program is using 3994504 bytes of Heap.
Program is using 4032400 bytes of Heap.
Program is using 4058464 bytes of Heap.
Program is using 4084656 bytes of Heap.
Program is using 4111128 bytes of Heap.
Program is using 4137336 bytes of Heap.
Program is using 4181240 bytes of Heap.
Program is using 4207304 bytes of Heap.
```

If your plot the data, memory growth becomes even more evident.

{with-memory-leak.png}

If you curious how I've plotted the data, read on. If not please skip to the next section. I am saving the stats being outputted into a JSON file, and then read it in and plotted it with a few lines of of Python. I've kept it on a separate brunch to avoid confusion, but you can check it out here: https://github.com/akras14/memory-leak-example/tree/plot

Relevant parts are:

```JavaScript
var fs = require('fs');
var stats = [];

//--- skip ---

var heapUsed = process.memoryUsage().heapUsed;
stats.push(heapUsed);

//--- skip ---

//On ctrl+c save the stats and exit
process.on('SIGINT', function(){
  var data = JSON.stringify(stats);
  fs.writeFile("stats.json", data, function(err) {
    if(err) {
      console.log(err);
    } else {
      console.log("\nSaved stats to stats.json");
    }
    process.exit();
  });
});
```

and

```Python
#!/usr/bin/env python

import matplotlib.pyplot as plt
import json

statsFile = open('stats.json', 'r')
heapSizes = json.load(statsFile)

print('Plotting %s' % ', '.join(map(str, heapSizes)))

plt.plot(heapSizes)
plt.ylabel('Heap Size')
plt.show()
```

You can check out the **plot** branch, and run the program as usual. Once you are finished run `python plot.py` to generate the plot. You'll need to have Matplotlib library installed on your machine for it to work.

<a name="heapdump"></a>
## Step 2. Take at least 3 Heap dumps
OK, so we've reproduce the problem, now what? Now we need to figure out where the problem is and fix it :)

You might have noticed the following lines in my sample program above:

```JavaScript
require('heapdump');
// ---skip---

//3. Get Heap dump
process.kill(process.pid, 'SIGUSR2');

// ---skip---
```

I am using a node-heapdump module, that you can find here: https://github.com/bnoordhuis/node-heapdump

In order to use node-heapdump, you just have to:

1. Install it.
2. Require it at the top of your program
3. Call `kill -USR2 <pid>` on Unix like platforms

If you've never see the `kill` part before, it's a command in Unix that allows you to (among other things) send a custom signal(aka User Signal) to any running process. Node-heapdump is configured to take a Heap dump of the process, any time it receives a **user signal two** hence the `-USR2`, followed by process id.

In my sample program I automate the `kill -USR2 <pid>` command by running `process.kill(process.pid, 'SIGUSR2');`, where `process.kill` is a node wrapper for `kill` command and `process.pid` gets the id for the current Node process. I run this command after each Garbage Collection to get a clean Heap dump.

Next section will cover how we can use the generated Heap dumps to isolate the memory leak.

<a name="find-problem"></a>
## Step 3. Find the problem

In step 2 we generated a bunch of heap dumps, but we'll need at least 3 at the minimum, and you'll soon see why.

Once you have your heap dumps. Head over to Google Chrome, and open up Chrome Developer tools(F12 on Windows or Command + Options + i on Mac).

Once in the Developer Tools Navigate to "Profiles" tab, select "Load" button at the bottom of the screen, navigate to the first Heap Dump that you took, and select it. The heap dump will load into the Chrome view as follows:

{1st-Heap-Dump}

Go ahead an load 2 more heap dumps, into the view. For example you can use the last 2 heap dumps that you've taken. The most important thing is that heap dumps must be loaded in the order that they were taken. Your Profiles tab should look similar to the following.

{3-Heap-Dumps}

As you can tell from the above image, the Heap continues to grow a little over time.

### One magic view to rule the all
The Profiles tab has a lot of view, and it's easy to get lost in them. There is one view, however, that I found the most helpful.

Click on the last Heap dump that you have taken, it will immediately put you into the "Summary" view. To the left of the "Summary" drop down, you should see another drop down that says "All". Click on it and select "Objects allocated between heapdump-YOUR-FIRST-HEAP-DUMP and heapdump-YOUR-SECOND-TO-LAST-HEAP-DUMP", as can be see in the image bellow.

{3-Heap-Dump-View}

What it will do, is show you all of the objects that were allocated sometimes between your first heap dump, and your second to last heap dump, that are still present in your final heap dump, even though they should have been picked up by Garbage collection.

Pretty amazing stuff, and really easy to over look.

### Ignore anything in brackets, such as (string), at least at first

After I completed the steps outline above for my sample app, I ended up with the following view.

Note that the **shallow size** represents the size of the object itself, while **retained size** represents the size of the object and all of it's children.

{memory-leak}

There appear to be 5 entries that were retained in my last snapshot that should have not been there: (array), (compiled code), (string), (system), and SimpleClass.

Out of all of them only SimpleClass looks familiar, since it came from the following code in the sample app.

```JavaScript
var randomObject = new SimpleClass(randomData);
```

It may be tempting to start looking through the (array) or (string) entries first. All objects in Summary view are grouped by their constructor names. In case of array or string, those are constructors internal to the JavaScript engine. And while your program is most likely holding on to some data that was created through those constructors, you would also get a lot of noise there.

That is why it's much better to skip those at first, and instead to see if you can spot any more obvious suspects, such as SimpleClass constructors in the sample app.

Clicking on the drop down arrow in the SimpleClass constructor, and selecting any of the created objects from the resulting list, will populate the retainer path in the lower part of the window. From there it's very easy to track that the leakyData array was holding on to our data.

If you are not as fortunate in your app, as I was in my sample app. You might have to look and the internal constructors (such as strings) and try to figure out what is causing the memory leak from there. The trick there would be to try to identify objects that show up a lot in some of the internal constructors groups, and try to use that as a hint pointing to a suspected memory leak.

<a name="confirm"></a>
## Step 4. Confirm that the issue is resolved

After you have identified and fixed a suspected memory leak, you should see a big difference in your heap usage.

If we uncomment the following line, in the sample app:

```JavaScript
cleanUpData(leakyData, randomObject); //<-- Forgot to clean up
```

And re-run the app as described in the Step 1, well observe the following output:

```
Program is using 3756664 bytes of Heap.
Program is using 3862504 bytes of Heap.
Program is using 3763208 bytes of Heap.
Program is using 3763400 bytes of Heap.
Program is using 3763424 bytes of Heap.
Program is using 3763448 bytes of Heap.
Program is using 3763472 bytes of Heap.
Program is using 3763496 bytes of Heap.
Program is using 3763784 bytes of Heap.
Program is using 3763808 bytes of Heap.
Program is using 3763832 bytes of Heap.
Program is using 3758368 bytes of Heap.
Program is using 3758368 bytes of Heap.
Program is using 3758368 bytes of Heap.
Program is using 3758368 bytes of Heap.
```

And if we plot the data it would look as follows:

{without-memory-leak.png}

Hooray, the memory leak is gone.

*Note that the initial spike in the memory usage is still there, this is normal while you wait for program to stabilize. Watch out for that spike in your analysis to make sure you are not interpreting it as a memory leak.*

<a name="links"></a>
## Links to some other resources

### Memory Profiling with Chrome DevTools

<iframe width="560" height="315" src="https://www.youtube.com/embed/L3ugr9BJqIs" frameborder="0" allowfullscreen></iframe>

Most of the stuff you've read in this article has been taken from this video. In the matter of fact, the only reason this article exists, is because had to watch this video 3 times over the course of two weeks to spot (what I believe to be) the key points, and I wanted to save others the pain and time. I would highly recommend watching this video to supplement this post.

### Another helpful tool - memwatch-next

This is another cool tool, that I think is worth mentioning. You can read more about some of the reasoning for it here (short read, worth your time): https://hacks.mozilla.org/2012/11/tracking-down-memory-leaks-in-node-js-a-node-js-holiday-season/

Or just go straight to the repo: https://github.com/marcominetti/node-memwatch

To save you a click, you can install it with `npm install memwatch-next`

And then use it with two events:
```JavaScript
var memwatch = require('memwatch-next');
memwatch.on('leak', function(info) { /*Log memory leak info, runs when memory leak is detected */ });
memwatch.on('stats', function(stats) { /*Log memory stats, runs when V8 does Garbage Collection*/ });

//It can also do this...
var hd = new memwatch.HeapDiff();
// Do something that might leak memory
var diff = hd.end();
console.log(diff);
```

The last console log will output something like the following, showing you what types of objects has grown in memory.

```JSON
{
  "before": { "nodes": 11625, "size_bytes": 1869904, "size": "1.78 mb" },
  "after":  { "nodes": 21435, "size_bytes": 2119136, "size": "2.02 mb" },
  "change": { "size_bytes": 249232, "size": "243.39 kb", "freed_nodes": 197,
    "allocated_nodes": 10007,
    "details": [
      { "what": "String",
        "size_bytes": -2120,  "size": "-2.07 kb",  "+": 3,    "-": 62
      },
      { "what": "Array",
        "size_bytes": 66687,  "size": "65.13 kb",  "+": 4,    "-": 78
      },
      { "what": "LeakingClass",
        "size_bytes": 239952, "size": "234.33 kb", "+": 9998, "-": 0
      }
    ]
  }
}
```

Pretty cool.

### JavaScript Memory Profiling from Developer.chrome.com

https://developer.chrome.com/devtools/docs/javascript-memory-profiling

Definitely a must read. It covers all of the subjects that I've touched up on, and many more in much greater detail with much greater accuracy :)

Don't over look this talk by Addy Osmani at the bottom, where he mentions a bunch of debugging tips and resource.

<iframe width="560" height="315" src="https://www.youtube.com/embed/LaxbdIyBkL0" frameborder="0" allowfullscreen></iframe>

You can get slide to it here: https://speakerdeck.com/addyosmani/javascript-memory-management-masterclass and sample code here: https://github.com/addyosmani/memory-mysteries

<a name="summary"></a>
## Summary

1. Trigger Garbage Collection manually when trying to reproduce and identify a memory leak. You can run Node with `--expose-gc` flag and call `global.gc()` from your program.
2. Take at least 3 Heap Dumps using https://github.com/bnoordhuis/node-heapdump
3. Use 3 Heap Dump technique to isolate the memory leak
4. Confirm that memory leak is gone
5. Profit
