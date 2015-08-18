/* globals React */

'use strict';

// var { div, select, option, h1 } = React.DOM;

var div = React.DOM.div;
var select = React.DOM.select;
var option = React.DOM.option;
var h1 = React.DOM.h1;

var comboBox = (
  div({
      onClick: function () {
        window.alert('foo');
      }
    }, 
    h1({className: 'hot'}, 'hello'),
    select({},
      option({}, 'foo'),
      option({}, 'bar'),
      option({}, 'baz')
    )
  )
);

React.render(comboBox, document.getElementById('app'));
