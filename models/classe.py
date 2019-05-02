# -*- coding: utf-8 -*-

from odoo import models, fields, api
from stdnum.mx.rfc import _name_blacklist

class classe(models.Model):
    _name = 'classe'
    
    name = fields.Char('name')
    level = fields.Selection([('seconde', 'Seconde'),('première', 'Première'),('terminale', 'Terminale'),],'level', default='seconde')
    professeur_ids = fields.Many2many('res.partner', string = 'Professeur')
    eleve_ids = fields.One2many('eleve', 'classe_id')
    agenda_ids = fields.One2many('agenda', 'classe_id')
    