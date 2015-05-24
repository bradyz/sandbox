function scroll(x) {
  x = typeof x !== 'number' ? 0 : x;

  var scrolltext = document.getElementById('scrollme');
  var text = '&nbsp' + scrolltext.innerHTML;
  scrolltext.innerHTML = text;

  if(text.length > scrolltext.offsetWidth) {
    text = text.substring(text.indexOf(' '));
    scrolltext.innerHTML = text;
  }

  window.setTimeout(scroll, 50, ++x);
}
