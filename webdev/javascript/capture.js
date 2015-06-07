'use strict';

$(function () {
  var boxes = $('.box');
  for(var i = 0; i < boxes.length; ++i) { 
    boxes[i].addEventListener('click', function () {
      window.alert($(this).text());
    }, true);
  }
});
