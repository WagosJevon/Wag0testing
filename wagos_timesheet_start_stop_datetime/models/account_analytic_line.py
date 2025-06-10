# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class AccountAnalyticLine(models.Model):
    _inherit = 'account.analytic.line'

    @api.depends('start_time', 'end_time')
    def _get_unit_amount(self):
        for rec in self:
            unit_amount = 0
            if rec.start_time and rec.end_time:
                duration = rec.end_time - rec.start_time
                unit_amount = duration.total_seconds() / 3600.0
            rec.unit_amount = unit_amount

    start_time = fields.Datetime(string='Start Time')
    end_time = fields.Datetime(string='End Time')
    unit_amount = fields.Float(compute='_get_unit_amount', store=True)
