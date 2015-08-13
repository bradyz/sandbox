'use strict'; 

function Person (name) {
  this.name = name;
}

Person.prototype.greet = function () {
  console.log('Hello! ' + this.name);
};

Person.prototype.rename = function (newName) {
  this.name = newName;
};

module.exports = Person;
