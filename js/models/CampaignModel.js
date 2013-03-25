$(function () {
		Campaign = StackMob.Model.extend({
				schemaName: 'campaign'
				,defaults: function() {
						return {
								powerlevel: "feet-in-the-water"
								,name: "My First Campaign"
								,cityname: "Metropolis"
						}
				}
		});

		CampaignCollection = StackMob.Collection.extend({
				model: Campaign
		});

		Player = StackMob.Model.extend({
				schemaName: 'player'
				,defaults:function() {
						return {
								name: ""
								,email: ""
								,charactername: ""
								,template: ""
						}
				}
		});
});