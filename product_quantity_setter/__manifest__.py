# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Product Stock Quantity Setter',
    'version': '1.0',
    'category': 'Extra Tools',
    'sequence': 0,
    'author': 'coobitech',
    'license': 'AGPL-3',
    'summary': 'This module allows you to create products and set Weight,'
               ' Internal Reference, Name, Barcode and Stock location quantity.'
               ' Updating mentioned fields is also possible. Works fine with multi warehouses.',
    'description': "",
    'depends': ['base', 'sale', 'stock', 'contacts'],
    'data': [
        'views/product_utility.xml'
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False
}
