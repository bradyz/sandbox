var timeit = function (func, that, args) {
  var now = new Date().getTime();

  if(typeof args === 'undefined') {
    func.apply({}, that);
  } else {
    func.apply(that, args);
  }

  var then = new Date().getTime();

  console.log(then - now + " ms elapsed.");
};

timeit(console.log, [123]);
