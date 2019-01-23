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
		}
	]
