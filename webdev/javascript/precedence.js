'use strict'; 

var Ninja = function () {
  this.truth = true;

  this.checkTruth = function () { 
    return this.truth;
  };
};

Ninja.prototype.checkTruth = function () { 
  return !this.truth;
};

var lulu = new Ninja();

console.log(lulu.checkTruth());                   // true
