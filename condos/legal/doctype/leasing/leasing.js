// Copyright (c) 2019, Yefri Tavarez and contributors
// For license information, please see license.txt

frappe.ui.form.on('Leasing', {
	tc_name: frm => {
		frm.call("render_terms_and_conditions_template")
	}
});
