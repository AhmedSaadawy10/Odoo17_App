{
    "name": "Hospital Management System",
    "author": "Ahmed Saadawy",
    "description": "This is the System for Management Hospital and assignment patients Information",
    "data": [
        "reports/patient_print.xml",
        "security/ir.model.access.csv",
        "security/hms_security.xml",
        "views/base_menus.xml",
        "views/hms_patient_view.xml",
        "views/hms_department_view.xml",
        "views/hms_doctor_view.xml",
        "views/customer_inherit_view.xml",
        'wizard/add_history_wizard.xml',

    ],
    'depends': ['base', 'web', 'crm'],
}
