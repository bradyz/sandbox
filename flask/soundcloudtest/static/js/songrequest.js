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
      _.bindAll(this, 'addOne', 'addAll', 'render');
      var handlers = {
          "success": this.addAll,
          "error": function() {console.log("fetch failed")}
         };
      
      Stocks.fetch(handlers);
    },

    addOne: function(stock) {
      var view = new StockView({model: stock});
      $("#song-list").append(view.el);
    },

    addAll: function() {
      Stocks.each(this.addOne);
     },

     refresh: function () {
       var handlers = {
         "success": this.addAll,
         "error": function() {console.log("fetch failed")}
       };
      
       Stocks.fetch(handlers);
     },

     createOnEnter: function(e) {
       var self = this;
       if(e.keyCode == 13) {
         $.get("/stocks/", {"ticker": $("#asdf").val()}, function(data) {
           _.each(JSON.parse(data), function(x){
             console.log(x);
             self.addOne(x);
           });
           $("#asdf").val("");
         });
       }
     }
  });

  window.Stocks = new StockList;
  window.App = new AppView;
});
