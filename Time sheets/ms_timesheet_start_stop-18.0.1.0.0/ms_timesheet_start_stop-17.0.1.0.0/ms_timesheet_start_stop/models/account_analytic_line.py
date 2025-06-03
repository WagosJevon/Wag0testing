# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
from datetime import datetime


class AccountAnalyticLine(models.Model):
    _inherit = 'account.analytic.line'

    start_time = fields.Datetime(string='Start Time')
    end_time = fields.Datetime(string='End Time')
    break_time = fields.Datetime(string='Break Time', readonly=True, copy=False)
    break_unit_amount = fields.Float(string='Break Time (Hour(s))')
    unit_amount = fields.Float(string='Worked Hours', compute='_compute_unit_amount', store=True)

    @api.depends('start_time', 'end_time', 'break_time', 'break_unit_amount')
    def _compute_unit_amount(self):
        for rec in self:
            unit_amount = 0.0
            if rec.start_time and (rec.break_time or rec.end_time):
                # Calculate base duration
                end = rec.end_time or rec.break_time
                duration = (end - rec.start_time).total_seconds() / 3600.0

                # Subtract break time
                if rec.break_unit_amount:
                    duration -= rec.break_unit_amount

                unit_amount = max(0.0, duration)
            rec.unit_amount = unit_amount

    def button_break(self):
        now = fields.Datetime.now()
        for rec in self.filtered(lambda r: r.start_time and not r.end_time and not r.break_time):
            rec.break_time = now

    def button_resume(self):
        now = fields.Datetime.now()
        for rec in self.filtered(lambda r: r.break_time):
            additional_break = (now - rec.break_time).total_seconds() / 3600.0
            rec.break_unit_amount += additional_break
            rec.break_time = False

    @api.constrains('end_time')
    def _check_break_time(self):
        for rec in self:
            if rec.end_time and rec.break_time:
                raise ValidationError(_(
                    'Please click "Resume" before ending the timesheet: %s') % rec.display_name)
