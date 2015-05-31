var myObject1 = function () {
  var val = 0;                      // scoped within function

  return {
    increment: function (inc) {
      return val += typeof inc === 'number' ? inc : 1;
    },
    getVal: function() {
      return val;
    }
  }
}();                                 // note the two parenthesis

// myObject.getVal() = 2;             // doesn't compile
// console.log(myObject1.val);        // undefined, hidden by scope
console.log(myObject1);               // { increment: [Function], getVal: [Function] }
console.log(myObject1.getVal());      // 0 
console.log(myObject1.increment());   // 1 
