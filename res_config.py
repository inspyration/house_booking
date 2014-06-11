# -*- coding: utf-8 -*-
from openerp.osv import fields, osv

class booking_config_settings(osv.osv_memory):
    _name = 'booking.config.settings'
    _inherit = 'res.config.settings'

    _columns = {
        'company_id': fields.many2one(
            'res.company',
            string="Company",
            required=True,
        ), 
        'booking_title': fields.char(
            string="Voucher title",
            size=1024,
        ),
    }

    def _default_company(self, cr, uid, context=None):
        user = self.pool.get('res.users').browse(cr, uid, uid, context=context)
        return user.company_id.id

    _defaults = {
        'company_id': _default_company,
    }