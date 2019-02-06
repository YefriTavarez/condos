# -*- coding: utf-8 -*-
# Copyright (c) 2019, Yefri Tavarez and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe import db, _

class Resident(Document):
	def validate(self):
		self.update_status()

	def after_insert(self):
		self.create_user()

	def on_trash(self):
		frappe.delete_doc_if_exists("User", self.user)

	def create_user(self):
		doctype = "User"
		if db.exists(doctype, self.user):
			return

		user = frappe.new_doc(doctype)

		user.update({
			"email": self.user,
			"first_name": self.first_name,
			"last_name": self.last_name,
			"full_name": self.full_name,
			"enabled": 1 if self.status == "Active" else 0,
			"username": self.full_name.replace(" ", "_"),
		})

		new_role = _("Resident")

		if not db.exists("Role", new_role):
			frappe.get_doc({
				"doctype": "Role",
				"role_name": new_role
			}).save(ignore_permissions=True)

		user.add_roles(new_role)
		user.save(ignore_permissions=True)

	def update_status(self):
		doctype = "User"
		if not db.exists(doctype, self.user):
			return

		user = frappe.get_doc(doctype, self.user)
		user.enabled = 1 if self.status == "Active" else 0

		user.save(ignore_permissions=True)




