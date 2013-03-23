$(function () {
		CampaignView = Backbone.View.extend({

				tagName : 'tr'

				,events : {
						"click .deleteCampaign" : "deleteCampaign"
				}

				,deleteCampaign : function() {
						this.model.destroy({
								success: function(model ) {
										app.alertSuccess( "Campaign " + model.get('name') + " succesfully deleted.");
								}

								,error: function(model, response ) {
										app.alertError("Campaign " + model.get('name') + " was not deleted. There was an error: " + response.error);
								}
						})
						return false;
				}

				,render :function() {
						$(this.el).html(this.template(this.model.toJSON()));
						return this;
				}
		});
});