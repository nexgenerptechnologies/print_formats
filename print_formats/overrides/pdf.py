import frappe

def set_custom_pdf_name(doc, method=None):
    if not frappe.flags.print_messages:
        # Get customer/supplier name based on doctype
        party_name = ""
        if hasattr(doc, "customer_name") and doc.customer_name:
            party_name = doc.customer_name
        elif hasattr(doc, "supplier_name") and doc.supplier_name:
            party_name = doc.supplier_name
        elif hasattr(doc, "customer") and doc.customer:
            party_name = doc.customer
        elif hasattr(doc, "supplier") and doc.supplier:
            party_name = doc.supplier
            
        file_name = f"{party_name} - {doc.name}" if party_name else doc.name
        
        # We can set the print heading, which Frappe often uses for the PDF filename 
        # when downloading via standard UI in newer versions.
        # Another approach is directly modifying frappe.response['filename'] if it's an export.
        if frappe.response and frappe.response.get("type") == "pdf":
            frappe.response["filename"] = f"{file_name}.pdf".replace(" ", "_")
        
        # Also set print_heading for good measure
        doc.custom_print_heading = file_name
