## TLDR;

1. Copy paste the script bellow, into your dev tools console (or add it to a snippet, read bellow for more info)
1. Select element for which you want to debug the nested scope
1. Run `scopeTree($0)` in your console

{demo-image}

```javascript
//Learned from http://stackoverflow.com/questions/23253506/get-dom-element-by-scope-id
function getElementByScopeId(id) {
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
    //Learned from https://twitter.com/akeemmclennon
    scope = angular.element(scope).scope();
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

To run the script, and get access
- Make new snippet
- Copy paste code
- Run Command + o (Ctrl + o on windows)
- Run Snippet

## How it works
### Get element via $0 trick
### Get element by scope ID trick
### Putting it all together
Recessively output methods until root scope is found.

