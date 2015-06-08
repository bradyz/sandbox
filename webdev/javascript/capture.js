/* global $  */  
'use strict';

$(function () {
  var boxes = $('.box');
  for(var i = 0; i < boxes.length; ++i) { 
    boxes[i].addEventListener('click', function () {
      return (function (el) {
        window.alert($(el).children('span').text());
      })(this);
    }, true);
  }
});
