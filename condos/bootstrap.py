# -*- coding: utf-8 -*-
# Copyright (c) 2019, Yefri Tavarez and contributors
# For license information, please see license.txt

from __future__ import unicode_literals

import frappe

def add_boot_info(bootinfo):
	from frappe import db

	default_company = db.get_single_value("Global Defaults",
		"default_company")

	if not default_company:
		company_list = db.sql_list("""
			Select
				name
			From
				`tabCompany`
		""")

		default_company = company_list and company_list[0]

	bootinfo.default_company = default_company

	# bootinfo.user = {
	# 	"defaults": frappe.defaults.get_defaults(),
	# }

	bootinfo.setup_complete = frappe.db.sql("""select name from
		tabCompany limit 1""") and 'Yes' or 'No'

	bootinfo.docs += frappe.db.sql("""select name, default_currency, default_terms,
		default_letter_head, default_bank_account, enable_perpetual_inventory from `tabCompany`""",
		as_dict=1, update={"doctype":":Company"})
