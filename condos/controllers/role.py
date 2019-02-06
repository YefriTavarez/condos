# -*- coding: utf-8 -*-
# Copyright (c) 2019, Yefri Tavarez and contributors
# For license information, please see license.txt

from __future__ import unicode_literals

import frappe

def create_simple_role(role):
	return frappe.get_doc({
		"desk_access": 1,
		"disabled": 0,
		"doctype": "Role",
		"role_name": role,
		"two_factor_auth": 0
	})
