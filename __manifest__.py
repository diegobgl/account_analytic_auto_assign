
{
    'name': 'Account Analytic Auto Assign',
    'version': '1.0',
    'category': 'Accounting',
    'summary': 'Asigna automáticamente cuentas analíticas de la cabecera a las líneas del asiento contable.',
    'description': 'Este módulo asigna automáticamente la cuenta analítica de la cabecera del asiento contable a las líneas que no tengan una cuenta analítica asignada.',
    'depends': ['account'],
    'data': [
        'views/account_move_view.xml',
        'data/server_action.xml',
    ],
    'installable': True,
    'application': False,
}
