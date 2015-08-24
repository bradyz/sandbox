'use strict';

var React = require('react');
var Router = require('react-router');

var Link = Router.Link;
var Route = Router.Route;
var RouteHandler = Router.RouteHandler;

var Login = require('./components/Login.js').Login;

var App = React.createClass({
  render: function () {
    return (

      <div className='nav'>
        <div>
          <Link to='app'>Home</Link>
        </div>
        <div>
          <Link to='login'>Login</Link>
        </div>
        <RouteHandler/>
      </div>

    );
  }
});

var routes = (  
  <Route name='app' path='/' handler={App}>
    <Route name='login' path='login' handler={Login}/>
  </Route>
);

Router.run(routes, function (Handler) {  
  React.render(<Handler/>, document.body);
});
