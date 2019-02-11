# -*- coding: utf-8 -*-
# Copyright (c) 2019, Yefri Tavarez and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

from frappe import db

class Leasing(Document):
	def autoname(self):
		self.name = frappe \
			.generate_hash(length=10) \
			.upper()

		if db.exists(self.doctype, self.name):
			self.autoname()

	def validate(self):
		pass

	def render_terms_and_conditions_template(self):
		if not self.tc_name:
			return

		template = db.get_value("Terms and Conditions",
			self.tc_name, "terms")

		# let's begin with a white sheet
		context = frappe._dict()

		# fetch linked docs
		for fieldname in ("resident", "property"):
			meta = self.meta

			docname = self.get(fieldname)
			if not docname:
				continue

			df = meta.get_field(fieldname)

			doctype = df.options

			doc = frappe.get_doc(doctype, docname)

			context.update(doc.as_dict())

		# override common fields in context
		context = self.as_dict()

		self.terms = frappe \
			.render_template(template, context)
