app_name = "print_formats"
app_title = "Professional Print Formats"
app_publisher = "Marketplace Publisher"
app_description = "Professional Print Formats for ERPNext"
app_email = "hello@example.com"
app_license = "mit"

fixtures = [
    {
        "dt": "Custom Field",
        "filters": [
            [
                "name", "in", [
                    "Stock Entry-tax_category",
                    "Stock Entry-taxes_and_charges"
                ]
            ]
        ]
    },
    {
        "dt": "Print Format",
        "filters": [
            ["module", "=", "Professional Print Formats"]
        ]
    }
]

doc_events = {
    "Sales Invoice": {
        "before_print": "print_formats.print_formats.overrides.pdf.set_custom_pdf_name"
    },
    "Purchase Order": {
        "before_print": "print_formats.print_formats.overrides.pdf.set_custom_pdf_name"
    },
    "Delivery Note": {
        "before_print": "print_formats.print_formats.overrides.pdf.set_custom_pdf_name"
    },
    "Sales Order": {
        "before_print": "print_formats.print_formats.overrides.pdf.set_custom_pdf_name"
    },
    "Stock Entry": {
        "before_print": "print_formats.print_formats.overrides.pdf.set_custom_pdf_name"
    }
}
