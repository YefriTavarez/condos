# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt

from __future__ import unicode_literals

import frappe

from frappe import _

default_lead_sources = ["Existing Customer", "Reference", "Advertisement",
	"Cold Calling", "Exhibition", "Supplier Reference", "Mass Mailing",
	"Customer's Vendor", "Campaign", "Walk In"]

def install(country=None):
	records = [
		{ 'doctype': 'Domain', 'domain': 'Distribution'},
		{ 'doctype': 'Domain', 'domain': 'Manufacturing'},
		{ 'doctype': 'Domain', 'domain': 'Retail'},
		{ 'doctype': 'Domain', 'domain': 'Services'},
		{ 'doctype': 'Domain', 'domain': 'Education'},
		{ 'doctype': 'Domain', 'domain': 'Healthcare'},
		{ 'doctype': 'Domain', 'domain': 'Agriculture'},
		{ 'doctype': 'Domain', 'domain': 'Non Profit'},

		{'doctype':"Address Template", "country": country},

		{'doctype': 'Mode of Payment',
			'mode_of_payment': 'Check' if country=="United States" else _('Cheque'),
			'type': 'Bank'},
		{'doctype': 'Mode of Payment', 'mode_of_payment': _('Cash'),
			'type': 'Cash'},
		{'doctype': 'Mode of Payment', 'mode_of_payment': _('Credit Card'),
			'type': 'Bank'},
		{'doctype': 'Mode of Payment', 'mode_of_payment': _('Wire Transfer'),
			'type': 'Bank'},
		{'doctype': 'Mode of Payment', 'mode_of_payment': _('Bank Draft'),
			'type': 'Bank'},


		{'doctype': "Print Heading", 'print_heading': _("Credit Note")},
		{'doctype': "Print Heading", 'print_heading': _("Debit Note")},


	]

	from frappe.modules import scrub
	for r in records:
		if not frappe.db.exists("DocType", r.get("doctype")):
			continue

		doc = frappe.new_doc(r.get("doctype"))
		doc.update(r)

		parent_link_field = ("parent_" + scrub(doc.doctype))
		if doc.meta.get_field(parent_link_field) and not doc.get(parent_link_field):
			doc.flags.ignore_mandatory = True

		try:
			doc.insert(ignore_permissions=True)
		except frappe.DuplicateEntryError as e:
			if e.args and e.args[0]==doc.doctype and e.args[1]==doc.name:
				pass
			else:
				raise

