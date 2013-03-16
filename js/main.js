var AppRouter = Backbone.Router.extend({

    routes: {
        ""                  : "index"
    }
    
		,initialize: function () {
			this.headerView = new HeaderView();
			$('.header').html(this.headerView.el);
    }
    
    ,index : function() {
    	$("#content").html(new InitialView().el);
    	this.headerView.selectMenuItem('home-menu');
    	}
});

utils.loadTemplate(['HeaderView', 'InitialView'], function() {
    app = new AppRouter();
    Backbone.history.start();
});