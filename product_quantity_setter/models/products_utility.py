import base64
from io import BytesIO

from xlrd import open_workbook

from odoo import models, fields
from odoo.exceptions import ValidationError


class ProductExcel(models.TransientModel):
    _name = 'product_quantity_setter.product_excel'

    product_excel_file = fields.Binary(string="Product excel file")

    def import_file(self):
        stock_locations = self.env['stock.warehouse'].search([])
        stock_location_names = []
        for stock_location in stock_locations:
            stock_location_names += [stock_location.name]
        try:
            inputx = BytesIO()
            inputx.write(base64.decodebytes(self.product_excel_file))
            book = open_workbook(file_contents=inputx.getvalue())
        except TypeError as e:
            raise ValidationError(u'ERROR: {}'.format(e))
        sheet = book.sheets()[0]
        products_data = self._convert_excel_to_dict(sheet)
        for index, row in enumerate(products_data):
            product = self.env['product.product'].search(
                [('name', '=', row['Name'])],
                limit=1)
            if not product:
                product = self.env['product.product'].create(
                    {'name': row['Name'], 'type': 'product'})
            if row.get('Internal Reference', ''):
                product.default_code = row.get('Internal Reference', '')
            if row.get('Barcode', ''):
                product.barcode = row.get('Barcode', '')
            for stock_location_name in stock_location_names:
                if row.get(stock_location_name, ''):
                    self._set_product_quantity(product, stock_location_name, row[stock_location_name])
            if row.get('Weight', ''):
                product.weight = row['Weight']

    def _convert_excel_to_dict(self, worksheet):
        first_row = []
        for col in range(worksheet.ncols):
            first_row.append(worksheet.cell_value(0, col))
        data = []
        for row in range(1, worksheet.nrows):
            elm = {}
            for col in range(worksheet.ncols):
                elm[first_row[col].strip()] = worksheet.cell_value(row, col)
            data.append(elm)
        return data

    def _set_product_quantity(self, product, wh, quantity):
        stock_loc = self.env['stock.warehouse'].search([('name', '=', wh)],
                                                       limit=1)
        stock_quant = self.env['stock.quant'].with_context(inventory_mode=True).search(
            [('product_id', '=', product.id), ('location_id', '=', stock_loc.lot_stock_id.id)])
        if not stock_quant:
            product_quant = self.env['stock.quant'].with_context(inventory_mode=True).create({
                'product_id': product.id,
                'inventory_quantity': float(quantity),
                'location_id': stock_loc.lot_stock_id.id,
            })
        else:
            qty = float(stock_quant.inventory_quantity)
            qty = qty + quantity
            stock_quant.write({'inventory_quantity': qty})
