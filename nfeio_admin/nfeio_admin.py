##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    Thinkopen Brasil
#    Copyright (C) Thinkopen Solutions Brasil (<http://www.tkobr.com>).
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

import openerp
from openerp import tools, api
from openerp.osv import osv, fields

class nfeio_servicomunicipio(osv.Model):
    _name = 'nfeio.servicomunicipio'
    _description = ''
    _order = 'name'
    
    _columns = {
        'name': fields.char('Code', size=64, required=True),
        'description': fields.char('Description', size=256),
        'country_id': fields.many2one('res.country', 'Country'),
        'state_id': fields.many2one('res.country.state', 'UF',
            domain="[('country_id','=',country_id)]"),
        'l10n_br_city_id': fields.many2one(
            'l10n_br_base.city', 'Municipio',
            domain="[('state_id','=',state_id)]"),
        'cnae_id': fields.many2one('l10n_br_account.cnae', u'CNAE'),
        'code_federal': fields.char('Federal Code', size=128),
        'code_municipal': fields.char('Municipal Code', size=128),
        'iss': fields.float('ISS'),
        'rt_ir': fields.float('IR Withholding'),
        'rt_pis': fields.float('PIS Withholding'),
        'rt_cofins': fields.float('COFINS Withholding'),
        'rt_csl': fields.float('CSL Withholding'),
        'rt_inss': fields.float('INSS Withholding'),
        'rt_iss': fields.float('ISS Withholding'),
        'date_start':fields.datetime('Date Start'),
        'date_end':fields.datetime('Date Start'), 
        'state':fields.selection([('updated','Updated'),('changed','Changed'),('inactive','Inactive')],)
        }
    
    _defaults = {
        'country_id': lambda self, cr, uid, c: self.pool.get('res.users').browse(cr, uid, uid, c).company_id.country_id.id,
        }
    
    _sql_constraints = [
        ('description_unique', 'unique(name)', u'The code must be unique.'),
        ]