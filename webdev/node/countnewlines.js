'use strict';
var fs = require('fs');

var str; 
try {
  str = fs.readFileSync(process.argv[2]).toString();
} catch (e) {
  console.log(e);
}

console.log(str.split('\n').length - 1);
