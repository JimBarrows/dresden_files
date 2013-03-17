var AppRouter = Backbone.Router.extend({

    routes: {
        ""                  : "index"
        ,"characters/add"   : "addCharacter"
        ,"campaigns/add"    : "addCampaign"
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
    	this.characterWorksheetView = new CharacterWorksheetView();
    	$("#content").html( this.characterWorksheetView.el);
    	}
    	
    ,addCampaign : function () {
    	this.campaignFormView = new CampaignFormView();
    	$("#content").html( this.campaignFormView.el);
    }
});

utils.loadTemplate(['HeaderView', 'InitialView', 'CharacterWorksheetView', 'CampaignFormView'], function() {
    app = new AppRouter();
    Backbone.history.start();
});