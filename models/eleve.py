# -*- coding: utf-8 -*-

from odoo import models, fields, api
from stdnum.mx.rfc import _name_blacklist
from datetime import *; from dateutil.relativedelta import *
import calendar

class eleve(models.Model):
    _name = 'eleve'
    
    @api.multi
    def name_get(self):
        #all logic goes here   
        result = []
        for record in self:
            name =  str(record.firstname) + ' ' + record.lastname
            result.append((record.id, name))
        return result
        
    
    name = fields.Char('name', default=name_get)
    age = fields.Integer('age')#, compute='_compute_total')
    firstname = fields.Char('firstname')
    lastname = fields.Char('lastname')
    birthdate = fields.Date('birthdate')
    classe_id = fields.Many2one('classe')
    
    #@api.depends('birthdate')
    #def _compute_total(self):
        #TODAY = date.today()
        #for record in self:
            #birthday = fields.Date.from_string(record.birthdate)
            #age = relativedelta(TODAY, birthday)
            #age = TODAY - age
            #age.strftime('%m/%d/%Y')
            #record.age = '%s-%s-%s' % (age.year, age.month, age.day)
            #print(TODAY)
        
        #return True
            
    
    