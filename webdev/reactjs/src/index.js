/* globals React */

'use strict';

// var React = require('react');
var App = React.createClass({
  render () {
    return (
      <ContentToggle buttonTitle='button 1'>
        <p>
          This is a really long summary
        </p>
      </ContentToggle>
    );
  }
});

var ContentToggle = React.createClass({
  getInitialState () {
    return {
      isOpen: true
    };
  },

  handleClick () {
    this.setState({
      isOpen: !this.state.isOpen
    });
  },

  render () {
    return (
      <div>
        <button onClick={this.handleClick}>{this.props.buttonTitle}</button>
        {this.state.isOpen && this.props.children}
      </div>
    );
  }
});

React.render(<App/>, document.getElementById('app'));
