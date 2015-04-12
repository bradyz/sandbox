$(function(){
  window.Stock = Backbone.Model.extend({
    idAttribute: "_id",
  });

  window.StockList = Backbone.Collection.extend({
    model: Stock,
    url: '/stocks',

    initialize: function() {
      this.fetch();
    }
  });

  window.StockView = Backbone.View.extend({
    tagName: "li",
    template: "<div class='song-entry'><%= title %></div>",

    initialize: function() {
      this.render();
    },

    render: function() {
      $(this.el).html(_.template(this.template, this.model.toJSON()));
    }
  });

  window.AppView = Backbone.View.extend({
    el: "#app",

    events: {
      "keydown #new-song":  "createOnEnter"
    },
    
    initialize: function() {
      _.bindAll(this, 'addOne', 'addAll', 'render');

      var handlers = {
          "success": this.addAll,
          "error": function() {console.log("fetch failed")}
         };
      
      // Songs.fetch(handlers);
    },

    addOne: function(stock) {
      var view = new StockView({model: stock});
      $("#song-list").append(view.el);
    },

    addAll: function() {
      Stocks.each(this.addOne);
     },

     createOnEnter: function(e) {
       if(e.keyCode == 13)
         console.log("123");
     }
  });

  window.Stocks = new StockList;
  window.App = new AppView;
});
