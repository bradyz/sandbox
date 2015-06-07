'use strict'; 

var Ninja = function () {
  this.truth = true;

  this.checkTruth = function () { 
    return this.truth;
  };

  this.dontThrow = function () {
    console.log('All is good');
  };
};

Ninja.prototype.checkTruth = function () { 
  return !this.truth;
};

Ninja.prototype.dontThrow = function () { 
  throw {
    name: 'BasicError',
    message: 'Does it reach here?'
  };
};

var lulu = new Ninja();

console.log(lulu.checkTruth());                   // true
lulu.dontThrow();                                 // all is good
