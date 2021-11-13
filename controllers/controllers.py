# -*- coding: utf-8 -*-
import odoo
from odoo import http
from odoo.http import request
import re
import base64

import logging
_logger = logging.getLogger(__name__)

CORS = '*'

class OdooDigitalPersonaApi(http.Controller):

    @http.route('/dp/api/get_connection', type="json", auth='none', cors=CORS)
    def odoo_dp_pi_version(self, **kw):
        version = odoo.release.version.split('.')

        fids = ''

        model = request.env['hr.employee'].sudo().search([])
        for rec in model:
            if rec.fid:
                fids = fids + str(rec.fid, 'utf-8') + ',' + rec.barcode + ';'
            else:
                fids = fids + '-' + ',' + rec.barcode + ';'

        return {
            "server_version": version[0] + "." + version[1],
            "server_version_info": [int(version[0]), int(version[1]), 0, "final", 0],
            "server_serie": version[0] + "." + version[1],
            "protocol_version": 1,
            "fids": fids
        }

    @http.route('/dp/api/save_fingerprint', type="json", auth='none', cors=CORS)
    def save_fingerprint(self, binary=None, badge=None, **kw):
        try:
            model = request.env['hr.employee'].sudo().search([('barcode', '=', badge)], limit=1)
            model.fid = binary
            return True
        except Exception as e:
            return str(e)

    @http.route('/dp/api/hr_check', type="json", auth='none', cors=CORS)
    def hr_check(self, badge=None, **kw):
        try:
            model = request.env['hr.employee'].sudo().search([('barcode', '=', badge)], limit=1)
            model.sudo().attendance_manual('hr_attendance.hr_attendance_action_my_attendances')
            return True
        except Exception as e:
            return str(e)

