import frappe
import json
from datetime import dates


@frappe.whitelist()
def get_gl(party):
    return frappe.db.sql("""
        SELECT SUM(tge.debit) - SUM(tge.credit) AS balance
        FROM `tabGL Entry` tge
        WHERE tge.is_cancelled = 0 AND tge.party = %(party)s
    """, {"party": party}, as_dict=True)
