var mammal = function(spec) {
  var that = {};
  
  that.get_name = function() {
    return spec.name || "No Name";                // doesnt return undefined
  };

  that.get_call = function() {
    return spec.call || "No Call";
  };

  return that;                                    // return two functions
};

var cat = function(spec) {
  var that = mammal(spec);

  that.get_call = function() {
    return "Meow";
  };

  that.purr = function() {
    return "Purr";
  };

  return that;
};

var dog = function(spec) {
  var that = mammal(spec);

  that.get_call = function() {
    return "Bark";
  };

  return that;
};

var pig = cat({name: "Pig"});
var skip = dog({name: "Skip"});

console.log(pig.get_name());
console.log(pig.get_call());
console.log(pig.purr());

console.log(skip.get_name());
console.log(skip.get_call());
// console.log(skip.purr());                        // no method error
