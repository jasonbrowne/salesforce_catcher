# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "salesforce_catcher"
app_title = "Salesforce Catcher"
app_publisher = "iXsystems.com"
app_description = "Tool to captcher SalesForce CRM info into ERPNext such as leads, contacts, accounts, opportunities."
app_icon = "octicon octicon-file-directory"
app_color = "blue"
app_email = "jason@ixsystems.com"
app_license = "MIT"
fixtures = ["SalesForceOpportunityDetails", "SalesForceOpportunityOtherDetails", "Sales Force Leads", "Sales Force Accounts" ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/salesforce_catcher/css/salesforce_catcher.css"
# app_include_js = "/assets/salesforce_catcher/js/salesforce_catcher.js"

# include js, css files in header of web template
# web_include_css = "/assets/salesforce_catcher/css/salesforce_catcher.css"
# web_include_js = "/assets/salesforce_catcher/js/salesforce_catcher.js"

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
# get_website_user_home_page = "salesforce_catcher.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "salesforce_catcher.install.before_install"
# after_install = "salesforce_catcher.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "salesforce_catcher.notifications.get_notification_config"

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
# 		"salesforce_catcher.tasks.all"
# 	],
# 	"daily": [
# 		"salesforce_catcher.tasks.daily"
# 	],
# 	"hourly": [
# 		"salesforce_catcher.tasks.hourly"
# 	],
# 	"weekly": [
# 		"salesforce_catcher.tasks.weekly"
# 	]
# 	"monthly": [
# 		"salesforce_catcher.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "salesforce_catcher.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "salesforce_catcher.event.get_events"
# }

