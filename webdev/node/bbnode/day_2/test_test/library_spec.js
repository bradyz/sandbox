'use strict'; 
/* global describe */
/* global it */

var expect = require('chai').expect;
var Library = require('./library.js');

describe('Library Test', function () {
  it('Should create an empty Library', function (done) {
    var lib = new Library();
    expect(lib.bookCount).equal(0);
    done();
  });

  it('Should add one book', function (done) {
    var lib = new Library();
    expect(lib.bookCount).equal(0);
    lib.add('Python');
    expect(lib.bookCount).equal(1);
    done();
  });

  it('Should return the right size', function (done) {
    var lib = new Library();
    expect(lib.bookCount).equal(0);
    lib.add('Python');
    expect(lib.all().length).equal(1);
    done();
  });

  it('Should return the right book', function (done) {
    var lib = new Library();
    lib.add('Python');
    lib.add('Ruby');
    lib.add('Java');
    expect(lib.show(1).book).equal('Python');
    done();
  });

  it('Should remove the right book', function (done) {
    var lib = new Library();
    lib.add('Python');
    lib.add('Ruby');
    lib.add('Java');
    lib.remove('Python');
    expect(lib.all().length).equal(2);
    done();
  });
});
