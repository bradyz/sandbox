'use strict';

var http = require('http');
var fs = require('fs');

function foo(req, res) {

  var stream = fs.createReadStream('wordsEn.txt');

  stream.on('open', function () {
    console.log('request inc');
    res.writeHead(200, {'Content-Type': 'text/plain'});
  });

  stream.on('data', function (data) {
    res.write(data);
  });

  stream.on('end', function () {
    res.end();
    console.log('request finished');
  });
}

var server = http.createServer(foo);

server.listen(3000);
