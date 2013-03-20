$(function() {
		Campaign = StackMob.Model.extend({
				schemaName: 'campaign'
				,defaults: function() {
						return {
								powerLevel: "Feet in the Water"
								,name: "My First Campaign"
								,cityName: "Metropolis"
						}
				}
		});

		CampaignCollection = StackMob.Collection.extend({
				model: Campaign
		});

		var CampaignList = new CampaignCollection;
		$.fn.serializeObject = function() {
				var o = {};
				var a = this.serializeArray();
				$.each(a, function() {
						if (o[this.name] !== undefined) {
								if (!o[this.name].push) {
										o[this.name] = [o[this.name]];
								}
								o[this.name].push(this.value || '');
						} else {
								o[this.name] = this.value || '';
						}
				});
				return o;
    };

		CampaignFormView = Backbone.View.extend({

				initialize: function () {
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
						console.debug('serialized version:' + $("#campaign-form").serializeObject());
						var newCampaign = new Campaign( $("#campaign-form").serializeObject());
						newCampaign.create({
								success: function(model) {
										console.debug('campaign object is saved, id: ' + model.get('campaign_id') + ', name: ' + model.get('name'));
								},
								error: function(model, response) {
										console.debug(response);
								}
						});
															
//						newCampaign.save( $("#campaign-form").serailizeArray());
						return false;
				}
		});

		CampaignListView = Backbone.View.extend({

				initialize: function () {
						this.render();
				}

				,render: function () {
						$(this.el).html(this.template());
						return this;
				}
		});
});