# -*- coding: utf-8 -*-

from odoo import models, fields, api
from stdnum.mx.rfc import _name_blacklist

class professeur(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'
    
    classe_ids = fields.Many2many('classe', string = "Classes")