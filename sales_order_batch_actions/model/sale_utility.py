from odoo import models


class SaleOrderBatch(models.Model):
    _inherit = 'sale.order'

    def batch_sales_order_confirm(self, timer=0):
        for sales in self:
            sales.action_confirm()

    def batch_sales_order_cancel(self, timer=0):
        for sales in self:
            sales.action_cancel()
