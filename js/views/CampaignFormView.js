$(function() {
		CampaignFormView = Backbone.View.extend({
		
				successMessage : _.template("Saved campaign <%= name %> in <%= cityname %> at power level <%= powerLevel %>")
		
				,errorMessage  :_.template("There was an error saving campaign <%= name %> in <%= cityname %> at power level <%= powerLevel %>.  The error was: <%= error %>")
		
				,initialize: function () {
						this.render();
				}
		
				,render: function () {
						$(this.el).html(this.template({campaign:null}));
						return this;
				}
		
				,events: {
						"submit #campaign-form" : "add"
				}
		
				,add : function(e) {
						var newCampaign = new Campaign( $("#campaign-form").serializeObject());
						var self = this;
						newCampaign.create({
								success: function(model) {
										app.alertSuccess( self.successMessage({ name: model.get('name') 
																														,cityname: model.get('cityname')
																														,powerLevel: model.get('powerLevel')}))
								}
								, error: function(model, response) {
										app.alertError( self.errorMessage( { name: model.get('name')
																												 , cityname: model.get('cityname')
																												 , powerLevel:  model.get('powerLevel')
																												 , response: response}))
								}
						});
						return false;
				}
		});
});
