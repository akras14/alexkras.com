## Introduction

Few months ago I had to debug a memory leak in Node.js. I found a good number of articles dedicated to the subject, but even after carefully reading some of them, I was still pretty confused on what exactly I should do to debug our memory leak.

My intent for this post is to be a simple guide for debugging a memory leak in Node. I will outline a single easy to follow approach, that should (in my opinion) be a starting point for any memory leak debugging in Node. For some cases this approach may not be enough, and I will link to some other resources that you may want to consider.

## Minimal Theory
JavaScript is a garbage collected language. Therefore, all memory used by a Node process is being automatically allocated and de-allocated by the V8 JavaScript engine.

How does V8 know when to de-allocated the memory? V8 Keeps a graph of all variables in the program, starting from a root node. There are 4 types of data types in JavaScript: Boolean, String, Number, and Object. First 3 are simple types, and they can only hold on to the data that is assigned to them (i.e. string of text). Objects, and everything else in JavaScript is an object (i.e. Arrays are Objects), can keep references (pointers) to other objects. Periodically V8 will walk through the Memory Graph, trying to identify groups of data that can no longer be reached from the root node. If it's is not reachable from the root node, V8 assumes that the data is no longer used and releases the memory. This process is called Garbage Collection.

Memory leak occurs in JavaScript when some no longer needed data is still reachable from the root node. V8 will assume that the data is still being used and will not release the memory. **In order to debug a memory leak we need to locate the data that is being kept by mistake, and make sure V8 is able to clean it up.**

It's also important to note that Garbage Collection does not run at all times. Normally V8 can trigger garbage collection when it deems appropriate. For example it could run a Garbage Collection periodically, or it could trigger an out of turn Garbage Collection if it senses that the amount of free memory is getting low. Node has a limited number for memory available to each process, so V8 has to use whatever it has wisely.

The later case of out of turn Garbage Collection could be a source of significant performance degradation. Imagine you have an app with a lot of memory leaks. Soon, Node process will begin to run out of memory, which would cause V8 to trigger an out of turn Garbage Collection. But since, most of the data can still be reach from the root node, very little of it will get cleaned up, keeping most of it in place. Sooner than later, Node process would run out of memory again, triggering another Garbage Collection. Before you know it, you app goes into a constant Garbage Collection cycle, just to try keeping the process functioning. Since V8 spends most of the time handling Garbage Collection, very little resources are left to run the actual program.

## Step 1. Reproduce and confirm the problem

As I've indicated earlier, V8 JavaScript engine has a complicated logic that it uses to determine when Garbage Collection should run. What it means in practical terms, that even though we can see a memory for the process continue to go up, we cannot be certain that we are witnessing a memory leak, until we know that Garbage Collection has ran, allowing unused memory to be cleaned up.

Thankfully, Node allows us to manually trigger Garbage Collection, and it is the first thing that we should do when trying confirm a memory leak. This can be accomplished by running Node with `--expose-gc` flag (i.e. `node --expose-gc index.js`). Once node is running in that mode, you can programmatically trigger a Garbage Collection at any time by calling `global.gc()` from your program.

You can also check the amount of memory used by your process by calling `process.memoryUsage().heapUsed`.

### Sample program
I've create a simple memory leak program, that you can see here: https://github.com/akras14/memory-leak-example

You can clone it, run `npm install` and then run `node --expose-gc index.js` to see it in action.

```
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

```
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

If you curious how I've plotted the data, read on. If not please skip to the next section. I've saved the stats that are being outputted into a json file, and then read it in and plotted it with a few lines of of Python. I've kept it on a separate brunch to avoid confusion, but you can check it out here: https://github.com/akras14/memory-leak-example/tree/plot

Relevant parts are:

```
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

```
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

## Step 2. Take at least 3 heap dumps

## Step 3. Find the problem

If we uncomment the line

```
cleanUpData(leakyData, randomObject); //<-- Forgot to clean up
```

And re run the test from Step 1, well observe the following output:

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

## Links to some other resources

https://youtu.be/L3ugr9BJqIs



Boolean, String, Number, Object - Key Value
Memory - Graph, Root Node
Object variables can point to others. Scalar can not point to anything else.
Shallow size - just the object
Retained size Shallow + all descendants
Garbage - all variables that cannot be reached from the root node
Clean up - Find all garbage clean up

Ignore code in (String) for now Array strings etc - Sorted by constructor name
Summary View - Between snapshots 1 and 2
Bottom will show retaining path - From root to the object that's being retained
Yellow Background - JavaScript Handle
Red - In DOM tree but can't access it from JS (Try to find a doc)
