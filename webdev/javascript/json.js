document.write('<script src="jquery.js"><\/script>');

var waitjQuery = function () {
  if(!jQuery) {
    window.settimeout(waitJquery, 100);
  }
}();

$.getJSON('test.json', function (data) {
  console.log(data);
});
