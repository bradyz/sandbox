'use strict';

let test = {
  foo: 1,
  bar: 2
};

let foo = test.foo,
    bar = test.bar;

console.log(foo, bar);

function* myGen (start, end, inc) {
  while (start < end) {
    yield start;
    start += inc;
  }
}

for (var a of myGen(0, 10, 1)) {
  console.log(a);
}
