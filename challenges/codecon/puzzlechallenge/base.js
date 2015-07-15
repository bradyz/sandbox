var readline = require('readline');
var rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
  terminal: false

});

rl.on('line', function (str) {
  var a = str.split(' ');
  console.log(parseInt(a[0]).toString(parseInt(a[1])).toUpperCase());
});

rl.on('close', function() {
  process.exit(0);

});

