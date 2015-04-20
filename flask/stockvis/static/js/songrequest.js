$(function(){
  window.Stock = Backbone.Model.extend({
    idAttribute: "_id",
  });

  window.StockList = Backbone.Collection.extend({
    model: Stock,
    url: '/stocks',

    initialize: function() {
    }
  });

  window.StockView = Backbone.View.extend({
    tagName: "tr",
    template: $("#stock-row").html(),

    initialize: function() {
      this.render();
    },

    render: function() {
      console.log(this.template);
      $(this.el).html(_.template(this.template, this.model.toJSON()));
    }
  });

  window.AppView = Backbone.View.extend({
    el: "#app",

    events: {
      "keydown #new-stock":  "createOnEnter"
    },
    
    initialize: function() {
      _.bindAll(this, 'addOne', 'render');
    },

    addOne: function(stock) {
      var mod = new Stock(stock);
      Stocks.add(mod)
      var view = new StockView({model: mod});
      $("#song-list").append(view.el);
    },

    createOnEnter: function(e) {
      var self = this;
      if(e.keyCode != 13) 
        return;

      $("#wait").show();

      var jqxhr = $.get("/stocks/", {"ticker": $("#asdf").val()}, function(data) {
        _.each(JSON.parse(data), function(d) {
          self.addOne(d);
        });

        $("#wait").hide();
      }).done(function() {
        console.log(123);
      }).always(function() {
        $("#wait").hide();
        $("#asdf").val("");
      });
    }
  });

  window.Stocks = new StockList;
  window.App = new AppView;
});
