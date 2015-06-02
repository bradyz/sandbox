function Person(name) {
  this.name = name;

  this.greet = function () {
    console.log(this.name);
  };
}

// var john = Person("john");
// john.greet();                   // undefined

var john = new Person("john");
var chad = new Person("chad");

john.greet();                   // john
chad.greet();                   // chad
