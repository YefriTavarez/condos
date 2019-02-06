from __future__ import unicode_literals
import frappe

# financials
class PartyFrozen(frappe.ValidationError): pass
class InvalidAccountCurrency(frappe.ValidationError): pass
class InvalidCurrency(frappe.ValidationError): pass
class PartyDisabled(frappe.ValidationError):pass
