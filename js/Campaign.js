$(function (){
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

CampaignView = Backbone.View.extend({
		tagName : 'tr'
		,render :function() {
				$(this.el).html(this.template(this.model.toJSON()));
				return this;
		}
});

CampaignListView = Backbone.View.extend({
		
		collection : new CampaignCollection()
		
		//	,tagName : 'table'
		
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