{
    'name': 'Batch Sales Order Actions',
    'version': '13.0',
    'summary': 'This module allows you confirm and cancel sale orders in batch.',
    'description': 'This module allows you confirm and cancel sale orders in batch.',
    'category': 'Sales',
    'author': 'coobitech',
    'website': 'www.coobi.tech',
    'maintainer': 'Arian Shariat',
    'license': 'LGPL-3',
    "data": [
        'views/sale_batch_confirm.xml',
        'views/sale_batch_cancel.xml',
    ],
    'images': ['static/description/banner.png'],
    'depends': ['sale', 'sale_management'],
    'installable': True,
    'auto_install': False,
    'application': True,

}
