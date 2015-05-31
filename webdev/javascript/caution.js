// WRONG: this will output "3" three times
var attachWrong = function (items) { 
  for(var i = 0; i < items.length; ++i) {
    items[i].wrong = function () {
      console.log(i);                           // closure keeps a reference to i
    };
  }
};

// RIGHT: this will output "0\n1\n2\n"
var attachRight = function(items) {
  for(var i = 0; i < items.length; ++i) {
    items[i].right = function (i) {
      return function() {
        console.log(i);                         // a new object with right i
      };
    }(i);
  }
};

var arr = [{}, {}, {}];                         // array of objects

attachWrong(arr);
attachRight(arr);

// wrong
for(var i = 0; i < arr.length; ++i) {
  arr[i].wrong();
}

// right
for(var i = 0; i < arr.length; ++i) {
  arr[i].right();
}
