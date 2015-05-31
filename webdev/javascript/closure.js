var quo = function (status) {
  return {
    getStatus: function() {
      return status;              // has access to the parameter
    }
  };
};

var a = quo("busy");              // no need to call new
var b = quo("free");

console.log(a.getStatus());       // busy
console.log(b.getStatus());       // free 
