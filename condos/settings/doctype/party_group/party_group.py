# -*- coding: utf-8 -*-
# Copyright (c) 2019, Yefri Tavarez and contributors
# For license information, please see license.txt

from __future__ import unicode_literals

import frappe
from frappe import _


from frappe.utils.nestedset import NestedSet
class PartyGroup(NestedSet):
	nsm_parent_field = 'parent_party_group';

	def on_update(self):
		self.validate_name_with_party()
		super(PartyGroup, self).on_update()
		self.validate_one_root()

	def validate_name_with_party(self):
		if frappe.db.exists("Party", self.name):
			frappe.msgprint(_("A party with the same name already exists"), raise_exception=1)

def get_parent_party_groups(party_group):
	lft, rgt = frappe.db.get_value("Party Group", party_group, ['lft', 'rgt'])

	return frappe.db.sql("""select name from `tabParty Group`
		where lft <= %s and rgt >= %s
		order by lft asc""", (lft, rgt), as_dict=True)
