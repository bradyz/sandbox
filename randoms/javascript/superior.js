Object.method('superior', function(name) {
  var that = this;
  var method = that[name];

  return function() {
    return method.apply(that, arguments);
  };
});
