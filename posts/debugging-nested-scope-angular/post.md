## Demo
<a href="http://www.alexkras.com/wp-content/uploads/scopeTree.gif"><img src="http://www.alexkras.com/wp-content/uploads/scopeTree.gif" alt="scopeTree" width="780" height="488" class="alignnone size-full wp-image-958" /></a>

## TLDR;

1. Copy paste the script bellow into your Chrome Dev Tools console or add it to a snippet (read bellow for more info on snippets).
1. Select element for which you want to debug the nested scope.
1. Run `scopeTree($0)` in your console to see the element, all the parent elements and their scope.

```javascript
function getElementByScopeId(id) {
  //Learned from http://stackoverflow.com/questions/23253506/get-dom-element-by-scope-id
  var elem;
  $('.ng-scope').each(function(){
      var scope = angular.element(this).scope();
      var scopeId = scope.$id;

      if(scopeId == id) {
          elem = this;
          return false; //Stop .each loop
      }
  });
  return elem;
}

function scopeTree(scope, recCount){
  if(scope instanceof HTMLElement){
    scope = angular.element(scope).scope(); //Learned from https://twitter.com/akeemmclennon
  }
  if(!recCount) recCount = 1;
  if(scope && scope.$id){
    var pointerString = '';
    for(var i = 0; i < recCount; i++){
      pointerString += '>';
    }
    console.info(pointerString + ' Scope: ' + scope.$id);
    console.log(scope);
    var element = getElementByScopeId(scope.$id);
    if(element){
      console.log(element);
    } else {
      console.log('No Element');
    }
    console.log("\n\n");
    scopeTree(scope.$parent, ++recCount);
  }
}
```

## Run Script Quickly
Copying and pasting the script into console is fine to test things out, but it could get annoying if you want to use it often.  Luckily, Chrome Dev Tools has a cool and not very well know feature called "Snippets".

Snippets feature serve as a nice editor to easily test and debug small snippets of JavaScript code, as well as allows you to save those snippets for a later use.

<a href="http://www.alexkras.com/wp-content/uploads/snippets.png"><img src="http://www.alexkras.com/wp-content/uploads/snippets.png" alt="snippets" width="950" height="602" class="alignnone size-full wp-image-961" /></a>

**You can save the script above as a snippet and access it quickly**

1. Make new snippet (See image above). Name it "scopeTree" or anything else you'd like.
1. Copy paste above code into the snippet.
1. Open the snippet via a fuzzy select. Run **Command + o** (Ctrl + o on Windows) see the image bellow.
1. Run the snippet by hitting **Command + Enter** (Ctrl + Enter on Windows).
1. Select the element for which you want to debug the nested scope.
1. Enter `scopeTree($0)` in the console.

<a href="http://www.alexkras.com/wp-content/uploads/select.png"><img src="http://www.alexkras.com/wp-content/uploads/select.png" alt="select" width="945" height="598" class="alignnone size-full wp-image-964" /></a>

## How it works

There were 2 tricks that helped me to put this thing together.

### Get element via $0 trick

I learned this form a co-worker of mine [@akeemmclennon](https://twitter.com/akeemmclennon). In Chrome Dev Tools you can reference the last selected element via `$0`. Then you can get the angular scope for the selected element via: `angular.element($0).scope()`.

As you recall we call our function with `scopeTree($0)`, and use that to get the actual Angular element and it's scope.

Chances are you are using [AngularJS Batarang](https://chrome.google.com/webstore/detail/angularjs-batarang-stable/niopocochgahfkiccpjmmpchncjoapek?hl=en-US) for your development (if not, check it out). It already provides similar functionality, by exposing the $scope variable (just console log $scope after selecting an element) which is identical to running `$scope = angular.element($0).scope()` in your console.

You can actually use the Batarang's `$scope` variable instead of the `$0` with `scopeTree($scope)` function, if you so prefer.

### Get element by scope ID trick
As you probably know, in Angular every `$scope` maintains a reference to a parent scope aka `$scope.$parent`. But I wasn't sure if you could actually get the DOM element by specifying scope id.

Turns out you can, and I learned it by googleing and landing on this page:
[http://stackoverflow.com/questions/23253506/get-dom-element-by-scope-id](http://stackoverflow.com/questions/23253506/get-dom-element-by-scope-id)

Which led me to this piece of code.

```javascript
function getElementByScopeId(id) {
  //Learned from http://stackoverflow.com/questions/23253506/get-dom-element-by-scope-id
  var elem;
  $('.ng-scope').each(function(){
      var scope = angular.element(this).scope();
      var scopeId = scope.$id;

      if(scopeId == id) {
          elem = this;
          return false; //Stop .each loop
      }
  });
  return elem;
}
```

### Putting it all together
Once I could get the scope for selected element, and it's parent element via it parent element scope id, it was just a matter of recursively going up the parent tree, until the root node is found.

This allowed me to console log every element and it scope, which (in my opinion) provides for a very nice debugging experience.

### Why don't you just use the Batarang's nested scope view?
I am glad you asked.

Batarang does have a nested scope view, but I could never make it work for me. It just seemed too hard to visualize the scopes and elements that they was associated with. In addition, the expanded scope view that list all of scope's parameters and methods was just too long and hard to look through.

I prefer hovering over an element to see it highlighted in the web-page, as well as inspecting the scope object in Chrome Dev tools console.
