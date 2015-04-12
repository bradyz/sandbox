$(function(){
  window.Song = Backbone.Model.extend({
    idAttribute: "_id",
  });

  window.SongList = Backbone.Collection.extend({
    model: Song,
    url: '/songs',

    initialize: function() {
      // this.fetch();
    }
  });

  window.SongView = Backbone.View.extend({
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
      
      Songs.fetch(handlers);
    },

    addOne: function(song) {
      var view = new SongView({model: song});
      $("#song-list").append(view.el);
    },

    addAll: function() {
      Songs.each(this.addOne);
     },

     createOnEnter: function(e) {
       if(e.keyCode == 13)
         console.log("123");
     }
  });

  window.Songs = new SongList;
  window.App = new AppView;
});
