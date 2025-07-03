frappe.ui.form.on('User', {
    onload: function(frm) {
        if (!frm.doc.assigned_role && frm.doc.roles && frm.doc.roles.length > 0) {
            frm.set_value('assigned_role', frm.doc.roles[0].role);
        }
    }
});
