# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tinnakorn Group
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

# from filename import classname # in my folder
# from ubuntu_library import classname or filename # in ubuntu
# from module import filename or classname #in odoo
    
from openerp import models, fields, api #import file "model.py", "fields.py", "api.py"  from folder openerp
from dateutil.relativedelta import relativedelta
from datetime import datetime
from docutils.parsers import null
from openerp.exceptions import ValidationError

class res_partner(models.Model):
    _inherit = 'res.partner'

    supplier_type = fields.Selection([('00supplier', 'Buying now'), ('01okay', 'Okay, but not buy'), ('02not_choose', 'Still considering'),('03not_okay', 'Not Okay')],
        string="Supplier Type",
        help="มีการซื้อขายแล้วหรือไม่")
    email_print = fields.Char('Email Print')

    # @api.multi
    # def button_supplier(self):
    #     return self.write({'supplier_type': 'to_approve'})
    #
    # @api.multi
    # def button_okay(self):
    #     return self.write({'supplier_type': 'not_approve'})
    #
    # @api.multi
    # def button_not_choose(self):
    #     return self.write({'supplier_type': 'approved'})
    #
    # @api.multi
    # def button_not_okay(self):
    #     return self.write({'supplier_type': 'delete_requested'})



# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
