# -*- coding: utf-8 -*-

from odoo import models, fields


# Clients
class tdsiiut_device(models.Model):
    _name = 'tdsiiut.device'

    name = fields.Char("Nom", required=True)
    date_allocation = fields.Date("Date allocation")
    employee_id = fields.Many2one('res.partner', "Employé")
