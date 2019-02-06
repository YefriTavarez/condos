# -*- coding: utf-8 -*-
# Copyright (c) 2019, Yefri Tavarez and contributors
# For license information, please see license.txt

from __future__ import unicode_literals

import frappe

from frappe import db

def add_reqd_custom_fields_in_user():
	if db.exists("Custom Field",
		"User-dark_theme"):
		return

	from condos import user_custom_fields

	for docdict in user_custom_fields:
		frappe.get_doc(docdict) \
			.save(ignore_permissions=True)
