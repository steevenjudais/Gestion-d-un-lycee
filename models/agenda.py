# -*- coding: utf-8 -*-

from odoo import models, fields, api
from stdnum.mx.rfc import _name_blacklist

class agenda(models.Model):
    _name = 'agenda'
    
    @api.multi
    def name_get(self):
        #all logic goes here   
        result = []
        for record in self:
            name =  record.date_start[11:] + ' ' + record.date_stop[11:]
            result.append((record.id, name))
        return result
        
    
    name = fields.Char('name', default=name_get)
    date_start = fields.Datetime('date_start')
    date_stop = fields.Datetime('date_stop')
    room = fields.Char('room')
    classe_id = fields.Many2one('classe')
    cours_id = fields.Many2one('cours')
    