# -*- coding: utf-8 -*-


from openerp import models, fields, api, _
from datetime import datetime

class sup_crm(models.Model):
    _inherit = ['crm.phonecall']

    product_id = fields.Many2one(
        'product.product', 'Product')
    product_ids = fields.Many2many('product.product', string="Products")

    # partner_id = fields.Many2one('res.partner', string="Contact",
    #     domain=[('customer','=',True)])

