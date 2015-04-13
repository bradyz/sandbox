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
    tagName: "li",
    template: "<div class='stock-entry'><%=ticker%>: <%=Date%> $<%=High%></div>",

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
       if(e.keyCode == 13) {
         $("#wait").show();
         $.get("/stocks/", {"ticker": $("#asdf").val()}, function(data) {
           _.each(JSON.parse(data), function(d) {
             self.addOne(d);
           });
           $("#wait").hide();
         });
       }
     }
  });

  window.Stocks = new StockList;
  window.App = new AppView;
});
