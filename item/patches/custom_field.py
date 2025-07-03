# import frappe

# @frappe.whitelist(allow_guest=True)
# def add_custom():
#     """
#     Adds a custom Link field 'assigned_role' to the 'User' DocType which links to Role DocType.
#     """
#     if not frappe.db.exists("Custom Field", {"dt": "User", "fieldname": "Assign_role"}):
#         custom_field_doc = frappe.get_doc({
#             "doctype": "Custom Field",
#             "dt": "User",
#             "fieldname": "Assign_role",
#             "label": "Assign Role",
#             "default":"employee",
#             "fieldtype": "Data",
#             "insert_after": "middle_name",
#             "in_list_view": 1,
#             "read_only": 1
#         })
#         custom_field_doc.insert(ignore_permissions=True)
#         frappe.db.commit()
#         frappe.msgprint("✅ Custom Link field  added to User DocType.")
#     else:
#         frappe.msgprint("⚠️ Field already exists on User.")



# import frappe
# @frappe.whitelist(allow_guest=True)
# def logout_user():
#     frappe.local.login_manager.logout()
#     return {"message": "User logged out"}

# import frappe
# @frappe.whitelist(allow_guest=True)
# def field():

#     fields = frappe.get_all("Custom Field", filters={"dt": "User"}, fields=["fieldname"])
   
#     return fields
import frappe
from frappe import sendmail
from frappe import _

@frappe.whitelist(allow_guest=True)
def send_email_api(recipient, subject, message):
    try:
        sendmail(
            recipients=[recipient],
            subject=subject,
            message=message
        )

        return {
            "status": "success",
            "message": f"Email sent to {recipient}"
        }

    except Exception as e:
        return {
            "status": "error",
            "message": f"Failed to send email: {str(e)}"
        }
