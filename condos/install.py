# -*- coding: utf-8 -*-
# Copyright (c) 2019, Yefri Tavarez and contributors
# For license information, please see license.txt

from __future__ import unicode_literals

import frappe
from frappe import _, db

def before_install():
	"""runs before installation"""
	return check_setup_wizard_is_completed()


def after_install():
	"""runs after installation"""

	# add basic data
	add_party_groups()

	# create additional roles
	add_reqd_roles()

	# add customizations
	add_reqd_custom_fields()

	# save the changes to the database
	db.commit()

def add_party_groups():
	from . import party_groups

	for docdict in party_groups:
		doc = frappe.get_doc(docdict)

		doc.flags.ignore_children_type = True
		doc.flags.ignore_links = True
		doc.flags.ignore_validate = True
		doc.flags.ignore_permissions = True
		doc.flags.ignore_mandatory = True

		doc.insert()

def add_reqd_roles():
	"""adds default roles for the app to run"""

	from condos.controllers.role import create_simple_role

	doctype, role_list = "Role", (
		_("Tenant"),
		_("Leaser"),
		_("Supervisor"),
		_("Employee"),
		_("Maintainer"),
		_("Web User"),
	)

	for role in role_list:
		if db.exists(doctype, role):
			continue

		create_simple_role(role) \
			.save(ignore_permissions=True)

def add_reqd_custom_fields():
	from \
		condos \
		.controllers \
		.custom_field \
	import \
		add_reqd_custom_fields_in_user

	add_reqd_custom_fields_in_user()

def check_setup_wizard_is_completed():
	if db.get_default('desktop:home_page') == 'desktop':
		print()
		print("Please install Condos on a fresh site where the setup wizard is not completed")
		print()
		return False
