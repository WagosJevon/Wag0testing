# -*- coding: utf-8 -*-
{
    "name": "Start Stop Timesheet",
    "summary": "Add start, stop, and break time to track duration on timesheet entries.",
    "description": """
This module extends the analytic line model to support:
- Start and End time fields
- Break time handling (pause/resume)
- Automatic calculation of worked hours
    """,
    "author": "Miftahussalam",
    "website": "https://blog.miftahussalam.com/",
    "category": "Timesheets",
    "version": "18.0.1.0.0",
    "license": "LGPL-3",
    "depends": [
        "base",
        "analytic",
        "hr_timesheet",
    ],
    "data": [
        "views/account_analytic_line_views.xml",
    ],
    "demo": [],
    "images": [
        "static/description/images/main_screenshot.png",
    ],
    "installable": True,
    "application": False,
}
