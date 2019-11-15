#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    if os.environ.get('DEBUG', 'False') == 'True':
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings.dev")
    else:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings.production")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
