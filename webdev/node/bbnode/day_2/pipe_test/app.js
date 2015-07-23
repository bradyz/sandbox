'use strict';

var fs = require('fs');

function copyFile (srcPath, dstPath, func) {
  var reader = fs.createReadStream(srcPath);
  var writer = fs.createWriteStream(dstPath);

  writer.on('finish', func);

  reader.pipe(writer);
}

copyFile('../stream_test/wordsEn.txt', 'newfile.txt', function() {
  console.log('done');
});
