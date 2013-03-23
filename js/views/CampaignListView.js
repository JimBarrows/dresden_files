$(function() {
		CampaignListView = Backbone.View.extend({
		
				collection : new CampaignCollection()
				
				,initialize: function () {
						this.collection.bind('reset', this.render, this);
						this.collection.bind('add', this.render, this);
				}

				,render: function () {
						$(this.el).html(this.template());
						this.collection.each(function( campaign) {
								var view = new CampaignView({model: campaign});
								view.render();
								$("#campaign").append(view.el);
								return this;
						});
				}
		});
});