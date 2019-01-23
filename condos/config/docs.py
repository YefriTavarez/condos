# -*- coding: utf-8 -*-
# Copyright (c) 2019, Yefri Tavarez and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe

"""
Configuration for docs
"""

# source_link = "https://github.com/[org_name]/condos"
# docs_base_url = "https://[org_name].github.io/condos"
# headline = "App that does everything"
# sub_heading = "Yes, you got that right the first time, everything"

def get_context(context):
	context.brand_html = "Condos"
