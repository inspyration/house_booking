# -*- coding: utf-8 -*-
from openerp.osv import fields, osv

import logging
_logger = logging.getLogger('INSPY_booking')

class booking_config_settings(osv.osv_memory):
    _name = 'booking.config.settings'
    _inherit = 'res.config.settings'

    _columns = {
#         'company_id': fields.many2one(
#             'res.company',
#             string="Company",
#             required=True,
#         ), 
        'booking_title': fields.char(
            string="Voucher title",
            size=1024,
        ),
        'guarantee': fields.integer(
            string="Guarantee (%)",
        ),
        'deposit': fields.integer(
            string="Deposit",
        ),
    }

    def create(self, cr, uid, vals, context=None):
        config_id = osv.osv_memory.create(self, cr, uid, vals, context=context)
        self.write(cr, uid, config_id, vals, context=context)
        return config_id

#     def _default_company(self, cr, uid, context=None):
#         user = self.pool.get('res.users').browse(cr, uid, uid, context=context)
#         return user.company_id.id
# 
#     _defaults = {
#         'company_id': _default_company,
#     }

    def get_default_booking_title(self, cr, uid, fields, context=None):
        config_obj = self.pool.get('booking.config.settings')
        config_ids = config_obj.search(cr, uid, [], limit=1, order='id DESC', context=context)
        _logger.debug("config_ids: %s" % (config_ids))
        if config_ids:
            config = config_obj.browse(cr, uid, config_ids[0], context=context)
            _logger.debug("config: %s" % (config))
            if config:
                return {'booking_title': config.booking_title}
        return {}

    def set_default_booking_title(self, cr, uid, ids, context=None):
        config_obj = self.pool.get('booking.config.settings')
        config_ids = config_obj.search(cr, uid, [], limit=1, order='id DESC', context=context)
        config = self.browse(cr, uid, ids[0], context)
        config_obj.write(cr, uid, config_ids[0], {'booking_title': config.booking_title})

    def get_default_guarantee(self, cr, uid, fields, context=None):
        config_obj = self.pool.get('booking.config.settings')
        config_ids = config_obj.search(cr, uid, [], limit=1, order='id DESC', context=context)
        _logger.debug("config_ids: %s" % (config_ids))
        if config_ids:
            config = config_obj.browse(cr, uid, config_ids[0], context=context)
            _logger.debug("config: %s" % (config))
            return {'guarantee': config.guarantee}
        return {}

    def set_default_guarantee(self, cr, uid, ids, context=None):
        config_obj = self.pool.get('booking.config.settings')
        config_ids = config_obj.search(cr, uid, [], limit=1, order='id DESC', context=context)
        config = self.browse(cr, uid, ids[0], context)
        config_obj.write(cr, uid, config_ids[0], {'guarantee': config.guarantee})

    def get_default_deposit(self, cr, uid, fields, context=None):
        config_obj = self.pool.get('booking.config.settings')
        config_ids = config_obj.search(cr, uid, [], limit=1, order='id DESC', context=context)
        _logger.debug("config_ids: %s" % (config_ids))
        if config_ids:
            config = config_obj.browse(cr, uid, config_ids[0], context=context)
            _logger.debug("config: %s" % (config))
            return {'deposit': config.deposit}
        return {}

    def set_default_deposit(self, cr, uid, ids, context=None):
        config_obj = self.pool.get('booking.config.settings')
        config_ids = config_obj.search(cr, uid, [], limit=1, order='id DESC', context=context)
        config = self.browse(cr, uid, ids[0], context)
        config_obj.write(cr, uid, config_ids[0], {'deposit': config.deposit})

