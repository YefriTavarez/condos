# -*- coding: utf-8 -*-
# Copyright (c) 2019, Yefri Tavarez and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"module_name": "Assets",
			"color": "#ffcc00",
			"icon": "fa fa-building",
			"type": "module",
			"label": _("Assets")
		},
		{
			"module_name": "Relationships",
			"color": "#ffcc00",
			"icon": "fa fa-users",
			"type": "module",
			"label": _("Relationships")
		},
		{
			"module_name": "Setup",
			"color": "#ffcc00",
			"icon": "fa fa-cogs",
			"type": "module",
			"label": _("Setup")
		},
		{
			"module_name": "Financials",
			"color": "#ffcc00",
			"icon": "fa fa-book",
			"type": "module",
			"label": _("Financials")
		},
		{
			"module_name": "Maintenance",
			"color": "#ffcc00",
			"icon": "fa fa-paint-brush",
			"type": "module",
			"label": _("Maintenance")
		},
		{
			"module_name": "Party",
			"_doctype": "Party",
			"color": "#98d85b",
			"icon": "fa fa-user",
			"type": "link",
			"link": "List/Party/List",
			"label": _("Party")
		},
		{
			"module_name": "Relationships",
			"_doctype": "Resident",
			"color": "#98d85b",
			"icon": "fa fa-universal-access",
			"type": "link",
			"link": "List/Resident/List",
			"label": _("Resident")
		},
		{
			"module_name": "Account",
			"_doctype": "Account",
			"color": "#98d85b",
			"icon": "fa fa-file-text",
			"type": "link",
			"link": "Tree/Account",
			"label": _("Account")
		},
	]
