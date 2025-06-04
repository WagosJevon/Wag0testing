# -*- coding: utf-8 -*-
{
    "name": "Start Stop Timesheet",
    "summary": "Track start, stop, and break times on timesheets",
    "description": """
        This module enhances the Timesheet system by adding support for:
        - Start time
        - End time
        - Break tracking (pause and resume)
        Automatically calculates worked hours excluding break durations.
    """,
    "author": "Miftahussalam",
    "website": "https://blog.miftahussalam.com/",
    "category": "Human Resources/Timesheets",
    "version": "18.0.1.0.0",
    "depends": [
        "base",
        "analytic",
        "hr_timesheet",
    ],
    "data": [
        "views/account_analytic_line_views.xml",
    ],
    "assets": {
        # Optional if you later add JS or CSS for timesheet buttons
    },
    "demo": [],
    "images": [
        "static/description/images/main_screenshot.png",
    ],
    "license": "LGPL-3",
    "application": False,
    "installable": True,
}
