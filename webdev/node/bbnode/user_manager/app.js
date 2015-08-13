'use strict'; 

var express = require('express');
var app = express();
var bodyParser = require('body-parser');
var models = require('./models/index.js');

app.use(bodyParser.urlencoded({
  extended: true
}));

app.set('view engine', 'ejs');

app.post('/', function (req, res) {
  models.User.create({
    firstname: req.body.firstname,
    lastname: req.body.lastname,
    role: req.body.role,
    username: req.body.username
  }).done(function () {
    res.redirect('/');
  });
});

app.get('/', function (req, res) {
  models.User.findAll().done(function (users) {
    res.render('index', {
      allUsers: users
    });
  });
});

app.get('/edit/:id', function (req, res) {
  models.User.findById(req.params.id).done(function (row) {
    res.render('edit', {
      user: row
    });
  });
});

// this should be a put but i dont know how to use method override
app.post('/edit/:id', function (req, res) {
  models.User.findById(req.params.id).done(function(user) {
    user.updateAttributes({
      firstname: req.body.firstname,
      lastname: req.body.lastname,
      role: req.body.role,
      username: req.body.username
    }).done(function() {
      res.redirect('/');
    });
  });
});

app.listen(3000);
