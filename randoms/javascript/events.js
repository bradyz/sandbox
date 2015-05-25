var attach = function (nodes) {
  for(var i = 0; i < nodes.length; i += 1) {
    nodes[i].onclick = function(i) {
      return function(e) {
        alert(i);
      };
    }(i);
  }
};

attach(document.body.childNodes);
