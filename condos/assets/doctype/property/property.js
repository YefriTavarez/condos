// Copyright (c) 2019, Yefri Tavarez and contributors
// For license information, please see license.txt

frappe.ui.form.on('Property', {
	refresh: frm => {
		const events = [
			"add_custom_buttons",
		];

		$.map(
			events,
			frm
				.trigger
				.bind(frm)
		);
	},
	add_custom_buttons: frm => {
		const events = [
			"add_navigate_button",
		];

		$.map(
			events,
			frm
				.trigger
				.bind(frm)
		);
	},
	add_navigate_button: frm => {
		const {
			doc,
		} = frm;

		if (doc.geolocation) {
			frm.add_custom_button(
				__("Navigate to Location"),
				event => frm
					.trigger("navigate_to_geolocation")
			);
		}
	},
	navigate_to_geolocation: frm => {
		const { doc, } = frm,
			geolocation =
				JSON.parse(doc.geolocation);

		return geolocation
			.features
			.map(feature => {
				// console.table(feature);
				const coordinates = feature
					.geometry
					.coordinates;

				// http://maps.google.com/?q=[lat],[long]
				open(`http://maps.google.com/?q=${coordinates[1]},${coordinates[0]}`);
			});
	}
});
