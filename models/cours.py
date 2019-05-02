# -*- coding: utf-8 -*-

from odoo import models, fields, api
from stdnum.mx.rfc import _name_blacklist

class cours(models.Model):
    _name = 'cours'
    
    name = fields.Char('name')
    agenda_ids = fields.One2many('agenda', 'cours_id')
    