'use strict';

$(function () {
  $('a').click(function (e) {
    // e.preventDefault();                 // prevents '#' appended to url
    // e.stopPropagation();                // prevents 'box' 

    window.alert('a');

    // return false;                      // equivalent to both above
  });

  $('.box').click(function (e) {
    window.alert('box');                  // never gets called
  });
});
