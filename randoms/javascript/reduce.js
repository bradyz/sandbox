// add a new method called 'reduce'
Array.prototype.reduce = function (f, value) {
  for(var i = 0; i < this.length; ++i) {
    value = f(this[i], value);
  }
  return value;
};

// define a function to pass in
var add = function (a, b) {
  return a + b;
};

var a = [1, 2, 3, 4, 5];

// pass in initial value of 0
console.log(a.reduce(add, 0));
