$(function () {
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
});