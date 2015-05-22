Number.prototype.integer = function() {
   return Math[this < 0 ? 'ceiling' : 'floor'](this);
}

console.log(3.3.integer());           // using the newly defined integer method
