function Button (color) {
  this.color = color;
  this.press = function() {
    console.log(this.color);
  };
}

function makeButton (color) {
  var obj = {}
  obj.color = color;
  obj.press = function() {
    console.log(obj.color);
  };
  return obj;
}

var green = new Button('green');
var blue = makeButton('blue');
var red = makeButton('red');

green.press();
blue.press();
red.press();
