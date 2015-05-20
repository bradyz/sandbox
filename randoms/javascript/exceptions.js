var myAdd = function(a, b) {
  if (typeof a !== 'number' || typeof b !== 'number') {
    throw {
      name: 'TypeError',
      message: 'Non-numerical Params'
    };
  }

  return a + b;             // doesn't reach this point for exceptions
};

var tryAdd = function(a, b) {
  try {
    console.log(myAdd(a, b));
  } catch (e) {
    console.log(e.name + ' ' + e.message);
  }
};

tryAdd(1, 2);               // 3
tryAdd(1, 's');             // TypeError Exception
