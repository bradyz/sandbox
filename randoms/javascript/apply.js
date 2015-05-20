var myConstructor = function(str) {
  this.status = str;
};

myConstructor.prototype.getStatus = function() {                // class method
  return this.status;                                           // uses "this"
};

var myInstance = new myConstructor("Happy");                    // new instance
var myThis = {status: "Happy"};                                 // apply uses "this" 

console.log(myInstance.getStatus());                            // "Happy"
console.log(myConstructor.prototype.getStatus.apply(myThis));   // "Happy"
