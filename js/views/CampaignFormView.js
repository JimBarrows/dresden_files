$(function() {
		CampaignFormView = Backbone.View.extend({
		
				successMessage : _.template("Saved campaign <%= name %> in <%= cityname %> at power level <%= powerlevel %>")
		
				,errorMessage  :_.template("There was an error saving campaign <%= name %> in <%= cityname %> at power level <%= powerlevel %>.  The error was: <%= error %>")
		
				,currentTab : '#powerLevelTab'

				,initialize: function () {
/*						this.$('#campaignTabs a').click(function (e) {
								e.preventDefault();
								$(this).tab('show');
						})*/
						this.render();
				}
		
				,render: function () {
						$(this.el).html(this.template({campaign:this.model}));
						var self = this;
						this.model.get('players').forEach( function( player){
								var view = new PlayerRowView( {player_id: player});
								view.render();
								self.$("#playersTable").append( view.el);
						});
					
					//	var foo = this.$("#campaignTabs a[href='#powerLevel']");
						//		foo.tab('show');
						return this;
				}
		
				,events: {
						"change"                : "change"
						,"submit #campaign-form" : "save"
						,"click #playersTab" : "playersTab"
				}
		
				,change : function(event) {
						var target = event.target;
						var change = {};
						change[target.name] = target.value;
						this.model.set( change);
				}

				,save : function(event) {
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
						event.preventDefault();
						return false;
				}
			
				,playersTab : function(event) {
						this.currentTab = '#playersTab';
						this.$(this.currentTab).tab('show');
						event.preventDefault();						
						return false;
				}
		});
});
