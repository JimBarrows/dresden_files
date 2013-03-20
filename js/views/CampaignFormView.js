$(function() {
var CampaignFormView = Backbone.View.extend({

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
				var newCampaign = new Campaign();
				alert("newCampaign: " + $("#campaign-form").serailizeArray());
				return false;
		}
});
});