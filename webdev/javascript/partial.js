'use strict';

Function.prototype.partial = function() {
  var fn = this, 
      args = Array.prototype.slice.call(arguments);

  return function() {
    var arg = 0;

    for (var i = 0; i < args.length && arg < arguments.length; i++) {
      if (args[i] === undefined) {
        args[i] = arguments[arg++];
      }
    }

    console.log(args);

    return fn.apply(this, args);
  };
};

// as opposed to the curry function can take undefined arguments
var delay = setTimeout.partial(undefined, 10);

delay(function () {
  console.log('waiting 10 ms.');
});
