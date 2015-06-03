var _ = require('underscore');

function Developer (name) {
  this.name = name;
  this.says = function () {
    console.log(this.name);
  };
}

var brady = new Developer('brady');
var speak = brady.says;
var another = _.bind(speak, {name: 'greg'});

brady.speak();                                  // brady
another();                                      // greg
