/* globals React */

'use strict';

// var React = require('react');

class ContentToggle extends React.Component {
  render () {
    return (
      <div>
        <button>show stuff</button>
        <p>content</p>
      </div>
    );
  }
}

React.render(<ContentToggle/>, document.getElementById('app'));
