'use strict'; 
/* global describe */
/* global it */

var expect = require('chai').expect;

describe('Testing basic functionality', function () {
  it('Should add 3 and 4', function (done) {
    expect(2+3).equal(5);
    done();
  });
});
