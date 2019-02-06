// Copyright (c) 2019, Yefri Tavarez and contributors
// For license information, please see license.txt

frappe.ui.form.on('Resident', {
	refresh: frm => {
		frm.toggle_enable("user", frm.is_new());
	},
	email: frm => {
		frm.trigger("validate_email");
	},
	validate_email: frm => {
		// Validate email 
	},
	first_name: frm => {
		if (!frm.doc.first_name)
			return
		let name = frm.doc.first_name.trim().replace("  ", " ").toUpperCase();
		frm.set_value("first_name", name);

		frm.trigger("full_name");
	},
	last_name: frm => {
		if (!frm.doc.last_name)
			return

		let name = frm.doc.last_name.trim().replace("  ", " ").toUpperCase();
		frm.set_value("last_name", name);
		frm.trigger("full_name");
	},
	full_name: frm => {
		let name = [frm.doc.first_name, frm.doc.last_name];
		frm.set_value("full_name", name.join(" ")); 
	}
});
