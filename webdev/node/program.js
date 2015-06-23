'use strict';
var c = process.argv.splice(2, process.argv.length);
console.log(c.map(Number).reduce(function (a, b) {
  return a + b;
}));
