frappe.listview_settings["Resident"] = {
	add_fields: ["status"],
	get_indicator: doc => {
		if (doc.status == "Active") {
			return [__("Active"), "green", "status,=,Active"];
		} else if (doc.status == "Inactive") {
			return [__("Inactive"), "red", "status,=,Inactive"];
		}
	}
};