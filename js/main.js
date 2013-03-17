var AppRouter = Backbone.Router.extend({

    routes: {
        ""                  : "index"
        ,"characters/add"  : "addCharacter"
    }
    
		,initialize: function () {
			this.headerView = new HeaderView();
			$('.header').html(this.headerView.el);
    }
    
    ,index : function() {
    	$("#content").html(new InitialView().el);
    	this.headerView.selectMenuItem('home-menu');
    	}
    	
    ,addCharacter : function() {
    	this.characterPhasesWorksheetView = new CharacterPhasesWorksheetView();
    	$("#content").html( this.characterPhasesWorksheetView.el);
    	}
});

utils.loadTemplate(['HeaderView', 'InitialView', 'CharacterPhasesWorkesheet'], function() {
    app = new AppRouter();
    Backbone.history.start();
});