// Copyright (c) 2013, Frappe Technologies Pvt. Ltd. and contributors
// For license information, please see license.txt

frappe.require("assets/condos/js/financial_statements.js", function() {
	frappe.query_reports["Cash Flow"] = $.extend({},
		condos.financial_statements);

	frappe.query_reports["Cash Flow"]["filters"].push({
		"fieldname": "accumulated_values",
		"label": __("Accumulated Values"),
		"fieldtype": "Check"
	});
});
