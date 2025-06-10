<!--
# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class HelpdeskTicket(models.Model):
    _inherit = 'helpdesk.ticket'

    start_time = fields.Datetime(string='Start Time')
    end_time = fields.Datetime(string='End Time')
    unit_amount = fields.Float(compute='_compute_unit_amount', store=True)

    @api.depends('start_time', 'end_time')
    def _compute_unit_amount(self):
        for rec in self:
            if rec.start_time and rec.end_time:
                duration = rec.end_time - rec.start_time
                rec.unit_amount = duration.total_seconds() / 3600.0
            else:
                rec.unit_amount = 0.0
-->
