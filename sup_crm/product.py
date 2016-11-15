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
from openerp.tools.float_utils import float_round
from datetime import timedelta
from datetime import datetime
from openerp.exceptions import ValidationError
from dateutil.relativedelta import relativedelta

class product_template(models.Model):
    _inherit = 'product.template'

    # @api.one
    # def _phonecall_count(self):
    #     res = {}
    #     for product_tmp in self:
    #         res[product_tmp.id] = len(product_tmp.phonecall_ids)
    #     return res
    #
    # phonecall_count = fields.Integer(string='Phonecalls', compute='_phonecall_count')



# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
