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

var cat = mammal({name: "pig", call: "meow"});    // initialize mammal 
console.log(cat.get_name());
console.log(cat.get_call());
