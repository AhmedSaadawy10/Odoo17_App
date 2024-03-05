
{
    'name': "Todo App",
    'summary': """ """,
    'description': """first app""",
    'author': "Ahmed Saadawy",
    'category': 'Productivity',
    'version': '17.0.0.1.0',
    'depends': ['base',
                ],
    'application': True,
    'data': [
        'security/ir.model.access.csv',
        'views/base_menus.xml',
        'views/ticket.xml',
    ],
}