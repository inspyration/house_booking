# -*- coding: utf-8 -*-

{
    'name' : 'Booking management',
    'version' : '1.1',
    'author' : 'Alicia FLOREZ & Sébastien CHAZALLET',
    'category': 'Sales Management',
    'summary': 'Management of House, Guestrooms or hotel bookings.',
    'description' : """
        Management of House, Guestrooms or hotel booking.
    """,
    'website': 'http://www.inspyration.fr',
    'images' : [],
    'depends' : ['base', 'mail', 'crm'],
    'data': [
        'security/booking_security.xml',
        'security/ir.model.access.csv',
        'views/res_config_view.xml',
        'views/booking_view.xml',
        'report/voucher.xml',
        'views/email.xml',
    ],
    'js': [
    ],
    'qweb' : [
    ],
    'css':[
    ],
    'demo': [
    ],
    'test': [
    ],
    'installable': True,
    'auto_install': False,
}
