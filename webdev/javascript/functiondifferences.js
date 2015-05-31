try {
  f1();           // works
  f2();           // undefined
} catch (e) {
  console.log(e.name + ' ' + e.message);
}

// defined at runtime
function f1 () {
  console.log("f1");
}

// defined at parse time
var f2 = function () { 
  console.log("f2");
};

