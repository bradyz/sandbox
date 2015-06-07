'use strict';

var isZipCode = function (rhs) {
  return /^\d{5}-\d{4}$/.test(rhs);
};

console.log(isZipCode('78705-1234'));
console.log(isZipCode('abc-123'));
