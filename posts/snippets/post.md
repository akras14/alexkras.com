Google Chrome developer Tools has a code snippets feature that allows you to quickly write, test, save and re-use code snippets.

One way to test JavaScript code is to type it into Chrome Developer Tools console and hit enter. It will cause whatever you typed in to execute immediately. If you hit "Shift + Enter" instead, the cursor would move to a next line to allow you to enter code across multiple lines. The code will execute when you finally hit enter.

This is great for testing small functions, but I personally find it pretty annoying and hard to use for anything longer than 3 lines of code.

Thankfully, Google Chrome has code Snippet feature which solves this problem.

## Creating a code snippet

Code snippets is a special view that shows up in your Chrome developer tools. You can open the Developer Tools and navigate to Sources at the top menu, and Snippets in the left menu (See the image bellow).

You can right click in the left column, and select "new" from drop down menu to create a new snippet.

Once the new sniper is created, you can use the white space in the right column as a regular code editor.

Once you are done, you can run the snippet by either hitting the small play button to the right of the snippet, or hitting "Command + Enter" on Mac or "Control + Enter" on Windows.

You can also add break points to snippets, to help you debug your code, just like you would with any other JavaScript code loaded in Chrome Dev tools.

<a href="http://www.alexkras.com/wp-content/uploads/snippets.gif"><img src="http://www.alexkras.com/wp-content/uploads/snippets.gif" alt="snippets" width="780" height="504" class="alignnone size-full wp-image-974" /></a>

Once the snippet is saved you can open it by going back to the source tab, or by hitting a "Command + O" shortcut on Mac or "Control + O" on windows to open up fuzzy select, and typing in your snippet name.

After opening the snippet just hit "Command + Enter" shortcut on Mac or "Control + Enter" on Windows to run it.

## Summary

- Create new snippet by going to Sources -> Snippets in Chrome Dev Tools
- Open existing snippet via Fuzzy Select by hitting "Command + O" on Mac or "Control + O" on Windows. (Note, you can open regular JavaScript files loaded in your browser via the Fuzzy select).
- Use snippets for ad-hoc JavaScript testing and debugging
- Save your common debugging tasks as snippets and open them fast via Fuzzy select and then run them with "Command + Enter" on Mac or "Control + Enter" on windows.
- Research snippets collections created by others, such as: [https://github.com/bahmutov/code-snippets](https://github.com/bahmutov/code-snippets)
