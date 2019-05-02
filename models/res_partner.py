# -*- coding: utf-8 -*-

from odoo import models, fields


class tdsiiut_partner(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'

    employee_ref = fields.Char("Réf employé")
    device_ids = fields.One2many('tdsiiut.device', 'employee_id', "Devices")
