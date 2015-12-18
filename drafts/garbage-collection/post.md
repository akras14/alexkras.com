JavaScript engines (such as V8 that runs on Chrome and SpiderMonkey that runs Firefox) use garbage collection to manage memory. If you know what this sentence means, please feel free to skip to the next section.

As you probably heard by now, computer memory consists of ones and zeros, which is represented by one bit that can be on (one) or off(zero). 8 of those bits create one byte. When computer programs run, they have to request a needed number of bytes from the operating system. They also need to release(free up) those bytes back to the operating system, when they are done with them. If all programs would never release their memory, you would quickly run out of it, and computer would not be able to do any further operations.

In some of the lower level languages like C, it is the programmers responsibility to **manually** request memory from, and release memory back to the operating system. As you can imagine, this could become an involved process. As a result we have a large number of programming languages (Java, Python, JavaScript) that will automatically manage the memory for you. They will request the memory when it is needed, and release it back when your program is done with it. This process of releasing the memory back to the operating system is called **garbage collection**.

### How does a JavaScript engine know when to release the memory back to the operating system?

Imagine all of the memory used by a JavaScript program as a tree. It starts at the root of the tree and has a lot of branches growing out from it. JavaScript engine looks at all of the branches that are still can be reached from the root of the tree, and keeps them in memory.

Now imagine that the tree was growing on an spaceship where you could turn the gravity on and off, with a normal state having no gravity. If a tree branch were to get disconnected with no gravity, it would just hang in place still taking up almost as much room. If you were to turn the gravity on, the disconnected branch would fall to the ground, making it really easy to tell that it needs to be **collected** and put into **garbage**.

Also imagine that you were a gardner (aka JavaScript engine) and it was your job to clean up the disconnected branches in order to allow room for new branches to grow. To clean up the branches you would need to walk into the room, turn on the gravity, have the disconnected branches fall to the ground, pick them up, throw them out, and turn the gravity back off to make it easier for the tree to grow. Since you also have other responsibilities, you probably would only want to do this process periodically or when the space in the room gets too crowded, in order to have time to do other things.

That is almost exactly how the JavaScript garbage collection works. Except instead of the tree you have a "graph", which is kind of like a tree, except branches can have an unlimited number of connections to each other. You can think of it as a tree with a lot of branches tangled together. Even if the shortest path from the root of the tree to the branch may be cut, the branch would still hang in the air when the gravity turns on,  because it is connected to some other branch. Since it is hanging there, you would not be able to garbage collect it, until all of it's connections are cut.

**Key point: If a chunk of a memory can be reached from the root of the memory graph(tree), it will not be garbage collected.**

If you have a lot of branches that are stuck somehow to the tree, the room will eventually run out of space, and you as gardner/JavaScript engine would get a lot of alerts letting you know that the room is almost full. You would have to run into the room a lot, to turn on the gravity and clean up whatever branches may fall. But since most of the branches are tangled, your efforts will be mostly wasted, and the alerts will keep coming back. Eventually you will be so busy trying to clean up the room, that you will have very little time to do any other tasks and the performance of ALL your responsibilities would suffer (or your application will become slow in JavaScript terms).

That is essentially what Memory Leaks are. The goal of debugging memory leaks is trying to find what might be holding on to the memory (to what is the tree branch tangled) and trying to cut that connection.


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
