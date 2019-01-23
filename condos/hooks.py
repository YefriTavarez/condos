# -*- coding: utf-8 -*-
# Copyright (c) 2019, Yefri Tavarez and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "condos"
app_title = "Condos"
app_publisher = "Yefri Tavarez"
app_description = "Web application to manage the rental of apartments and houses."
app_icon = "fa fa-building"
app_color = "#ffcc00"
app_email = "yefritavarez@gmail.com"
app_license = "General Public License, v3"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/condos/css/condos.css"
# app_include_js = "/assets/condos/js/condos.js"

# include js, css files in header of web template
# web_include_css = "/assets/condos/css/condos.css"
# web_include_js = "/assets/condos/js/condos.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "condos.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "condos.install.before_install"
# after_install = "condos.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "condos.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"condos.tasks.all"
# 	],
# 	"daily": [
# 		"condos.tasks.daily"
# 	],
# 	"hourly": [
# 		"condos.tasks.hourly"
# 	],
# 	"weekly": [
# 		"condos.tasks.weekly"
# 	]
# 	"monthly": [
# 		"condos.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "condos.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "condos.event.get_events"
# }

