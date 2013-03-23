$(function () {
		CampaignView = Backbone.View.extend({

				tagName : 'tr'

				,render :function() {
						$(this.el).html(this.template(this.model.toJSON()));
						return this;
				}
		});
});