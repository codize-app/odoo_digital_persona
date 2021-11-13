# -*- coding: utf-8 -*-

from odoo import models, fields, api

class OdooDigitalPersona(models.Model):
    _inherit = 'hr.employee'

    fid = fields.Binary('Finger ID', help="Binary data of Finger ID form Digital Persona")
