'use strict';

Function.prototype.curry = function() {
  var fn = this,
      args = Array.prototype.slice.call(arguments);

  // similarly, 
  // args = [].slice().call(arguments);

  return function() {
    console.log(args.concat(Array.prototype.slice.call(arguments)));
    return fn.apply(this, args.concat(Array.prototype.slice.call(arguments)));
  };
};

// curry aka partial filling of arguments
String.prototype.csv = String.prototype.split.curry(/,\s*/); 

// split by regular expression
console.log(('brady, pig, cat').csv());
