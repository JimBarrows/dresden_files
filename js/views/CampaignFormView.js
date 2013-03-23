$(function() {
		CampaignFormView = Backbone.View.extend({
		
				successMessage : _.template("Saved campaign <%= name %> in <%= cityname %> at power level <%= powerlevel %>")
		
				,errorMessage  :_.template("There was an error saving campaign <%= name %> in <%= cityname %> at power level <%= powerlevel %>.  The error was: <%= error %>")
		
				,initialize: function () {
						this.render();
				}
		
				,render: function () {
						$(this.el).html(this.template({campaign:this.model}))
						return this;
				}
		
				,events: {
						"change"                : "change"
						,"submit #campaign-form" : "save"
				}
		
				,change : function(event) {
						var target = event.target;
						var change = {};
						change[target.name] = target.value;
						this.model.set( change);
				}

				,save : function() {
						var self = this;
						this.model.save(null, {
								success: function(model) {
										app.navigate('campaigns/edit/' + model.id, false);
										app.alertSuccess( self.successMessage({ name: model.get('name') 
																														,cityname: model.get('cityname')
																														,powerlevel: model.get('powerlevel')}));
										self.render();
								}
								,error: function(model, response) {
										app.alertError(  self.errorMessage( { name: model.get('name')
																													,cityname: model.get('cityname')
																													,powerlevel:  model.get('powerlevel')
																													,response: response}));
										self.render();
								}
						});
						return false;
				}
		});
});
