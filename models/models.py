# -*- coding: utf-8 -*-

from odoo import models, fields, api

class OdooDigitalPersona(models.Model):
    _inherit = 'hr.employee'

    fid = fields.Binary('Fid')
