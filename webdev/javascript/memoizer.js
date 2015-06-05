'use strict';

// from javascript the good parts
var memoizer = function (memo, fundamental) {
  var shell = function (n) {
    var result = memo[n];

    if(typeof result !== 'number') { 
      result = fundamental(shell, n);
      memo[n] = result;
    }
    return result;
  };
  return shell;
};

// from javascript ninja
Function.prototype.memoize = function (key) {
  this._values = this._values || {};

  if (this._values[key] === undefined) {
    this._values[key] = this.apply(undefined, arguments);   // 1st arg whatever
  }

  return this._values[key];
};

var fibonacci = memoizer([0, 1], function (shell, n) {
   return shell(n - 1) + shell(n - 2);
});

var isPrime = function (num) {
  for(var i = 2; i < num; ++i) {
    if(num % i === 0) {
      return false;
    }
  }

  return true;
};

console.log(fibonacci(10));
console.log(isPrime.memoize(5));
