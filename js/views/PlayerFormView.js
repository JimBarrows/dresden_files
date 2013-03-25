$(function() {
		PlayerFormView = Backbone.View.extend({
				
				initialize: function() {
						this.render();
				}

				,render: function() {
						$(this.el).html( this.template({ player: this.model}));
						return this;
				}

				,events: {
						"change" : "change"
						,"submit #player-form" : "save"
				}

				,change : function( event) {
						var target = event.target;
						var change={}
						change[target.name] = target.value;
						this.model.set( change);
				}

				,save : function() {
						var self = this;
						if( this.model.isNew()) {
								this.model.create({
										success: function( model) {
												app.campaignFormView.model.appendAndSave('players', [self.model.get('player_id')]);
												window.history.back();
										}
										,error: function(model,response) {
												app.alertError("Could not add player " + model.get('name') + " to campaign " + app.campaignFormView.model.get('name') + " because " +response);
										}
								});
						} else {
								this.model.save( null, {
										success: function( model) {
												app.campaignFormView.model.appendAndSave('players', self.model.get('player_id'));
												window.history.back();
										}
										,error: function(model,response) {
												app.alertError("Could not add player " + model.get('name') + " to campaign " + app.campaignFormView.model.get('name') + " because " +response);
										}
								});
						}
						return false;
				}
		});
});