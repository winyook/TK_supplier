# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 EANG COMPANY
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


{
    'name': 'Tinnakorn Module for Supplier logged calls',
    'version': '0.1',
    'category': 'Tools',
    'description': """
Module for Purchase Logged calls of Tinnakorn
Winyoo create 2016
    """,
    'author': 'Winyoo Kongkavitool',
    'depends': ['sale','product'], # depends--> look at folder's name
    'data': [#'security/sale_security.xml', # ระวังให้ประกาศ group(xml) ขึ้นก่อน data(csv) เผิ้อว่าตัว csv มันเรียก group
             #'security/ir.model.access.csv',
             #'data/crm.case.categ.csv',
             'crm_case_phone_form_view.xml',
            'product_view.xml',
            'view_partner_form.xml',
             ], #XML File that included in my module
             
    'demo': [
            ], #CSV Sample Data
    'installable': True, #  False mean no button to install
    'auto_install': False, #dangerous put auto_install
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
