$(function() {
		PlayerRowView = Backbone.View.extend({
				tagName: 'tr'
				,render: function() {
						this.model = new Player({player_id: this.options['player_id']});
						var self = this;
						this.model.fetch({
								success: function( model) {
										$(self.el).html(self.template({player: self.model}));
								}

								,error: function( model, response) {
										app.alertError( "There was an error retrieving player record id " + self.options['player_id'] + ".  Error is: " + response);
								}
						});
						return this;
				}
		});
});