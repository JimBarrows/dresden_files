AlertMessage = Backbone.Model.extend({
		defaults: {
				message : "this is a message"
				,type : ""
		}
});

AlertMessageCollection = Backbone.Collection.extend({

		model: AlertMessage
});

AlertListView = Backbone.View.extend({
		
		collection : new AlertMessageCollection()
		
		,initialize: function () {
				this.render();
				this.collection = new AlertMessageCollection();
				this.collection.bind('add', this.render, this);
		}

		,render :function() {
				$(this.el).html(this.template());
				var self = this;
				self.collection.each(function(alert) {
						var view = new AlertView({model: alert});
						view.render();
						$(self.el).append(view.el);
				});
				return this;
		}
});

AlertView = Backbone.View.extend({
		
		events: {
				'click .close' : 'close'
		}

		,render :function() {
				$(this.el).html(this.template(this.model.toJSON()));
				return this;
		}

		,close: function() {
				this.model.collection.remove(this.model);
		}
});