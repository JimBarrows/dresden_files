$(function() {
		var AppRouter = Backbone.Router.extend({
				
				routes: {
						""                  : "index"
						,"campaigns"        : "listCampaign"
						,"characters/add"   : "addCharacter"
						,"campaigns/add"    : "addCampaign"
						,"campaigns/edit/:id" : "editCampaign"
				}
				
				,initialize: function () {
						this.headerView = new HeaderView();
						$('.header').html(this.headerView.el);
						this.alertListView = new AlertListView();
						$("#alerts").html( this.alertListView.el);
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
		
				,listCampaign :function() {
						this.campaignListView = new CampaignListView();
						var self = this;
						this.campaignListView.collection.fetch({
								success: function( collection, response, options) {
										self.campaignListView.render();
								}
						});
						$("#content").html( this.campaignListView.el);
				}

				,editCampaign :function( id) {
						var campaign = new Campaign({campaign_id: id});
						var self = this;
						campaign.fetch({
								success: function(model, response, options){
										self.campaignFormView = new CampaignFormView({model :model});
										$("#content").html( self.campaignFormView.el);
								}

								,error: function(model, repsonse, options){
										app.alertError( "Could not retrieve model: " + model ?  model.toJSON() : "null" + " because " + response);
								}
						});
						this.headerView.selectMenuItem();
				}

				,alert : function(message) {
						this.alertListView.collection.add( new AlertMessage({message: message}));
				}

				,alertError : function( message) {
						this.alertListView.collection.add( new AlertMessage({message: message, type: "alert-error"}));
				}

				,alertSuccess : function( message) {
						this.alertListView.collection.add( new AlertMessage({message: message, type: "alert-success"}));
				}
				,alertInfo : function( message) {
						this.alertListView.collection.add( new AlertMessage({message: message, type: "alert-info"}));
				}
		});

		utils.loadTemplate(['HeaderView', 'AlertListView', 'AlertView', 'InitialView', 'CharacterWorksheetView', 'CampaignView', 'CampaignListView', 'CampaignFormView'], function() {
				app = new AppRouter();
				Backbone.history.start();
		});
});