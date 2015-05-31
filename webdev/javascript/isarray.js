var is_array = function (value) {
   return value &&
     typeof value === 'object' &&
     typeof value.length === 'number' &&
     typeof value.splice === 'function' &&
     !(value.propertyIsEnumerable('length'));
};

console.log(is_array([1, 2, 3]));
console.log(is_array({name: 'brady', age: 19}));
