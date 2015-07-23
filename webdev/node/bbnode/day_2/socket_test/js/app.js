'use strict';
/* global io */
/* global getMessage */

var socket = io.connect('http://arunchatserver.herokuapp.com');

socket.on('chat', function(msg) {
  getMessage(msg);
});

function sendMessage(message) {
  socket.emit('chat', message);
}
