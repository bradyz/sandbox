// has bind and bindall
var _ = require('underscore');

// basic constructor
function Developer (name) {
  this.name = name;
  this.says = function () {
    console.log(this.name);
  };
}

// create instance
var brady = new Developer('brady');

var speak = brady.says;
var speak1 = _.bind(speak, {name: 'greg'});
var speak2 = brady.says;

// binds brady object to all future says references
_.bindAll(brady, 'says');                       

var speak3 = brady.says;

brady.says();                                   // brady
speak();                                        // undefined
speak1();                                       // greg
speak2();                                       // undefined
speak3();                                       // brady
