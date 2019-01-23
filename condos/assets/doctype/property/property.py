# -*- coding: utf-8 -*-
# Copyright (c) 2019, Yefri Tavarez and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class Property(Document):
	pass
	# validate land against construction area
	# validate all numbers to be greater or equal than zero
	# validate monthly fee to be less than the property value
	# if it has garage it must me greater than zero
	# validate construction year to be less than current's
