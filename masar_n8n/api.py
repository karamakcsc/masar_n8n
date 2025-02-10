import frappe
# import json
# from datetime import dates


@frappe.whitelist()
def get_gl(party):
    return frappe.db.sql("""
        SELECT SUM(tge.debit) - SUM(tge.credit) AS balance
        FROM `tabGL Entry` tge
        WHERE tge.is_cancelled = 0 AND tge.party = %(party)s
    """, {"party": party}, as_dict=True)


# @frappe.whitelist()
# def get_sales_invoice():
#     return frappe.db.sql("""
#     SELECT SL.Customer, SL.posting_date,SL.company,SL.due_date ,SL.cost_center,SL.department, FROM `tab Sales Invoice`
# """)


@frappe.whitelist()
def get_sales_invoice(party):
    return frappe.db.sql("""
    SELECT * FROM `tabSales Invoice` WHERE customer = %(party)s
    """,{"party": party}, as_dict=True)