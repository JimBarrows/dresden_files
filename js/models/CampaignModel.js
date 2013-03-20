var Campaign = StackMob.Model.extend({
		schemaName: 'campaign'
		,defaults: function() {
				return {
						powerLevel: "Feet in the Water"
						,campaignName: "My First Campaign"
						,cityName: "Metropolis"
				}
		}
});

var CampaignCollection = StackMob.Collection.extend({
		model: Campaign
});

var CampaignList = new CampaignCollection;

