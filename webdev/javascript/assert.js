'use strict';

var assert = function (truth, msg) {
  if(truth) {
    console.log(msg);
  } else {
    throw {
      name: 'AssertError',
      message: 'Unexpected truth value.'
    };
  }
};

var one = 1;

var asdf = function () {
  assert(one === 1, 'one is one');
};

asdf();         // one is one

one = 2;

asdf();         // no output
