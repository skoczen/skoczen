#!/usr/bin/env python
from os.path import abspath, join, dirname
from sys import path
import os
import sys

PROJECT_ROOT = abspath(join(dirname(__file__), "project"))
APP_ROOT = abspath(join(dirname(__file__)))
path.insert(0, APP_ROOT)
path.insert(0, PROJECT_ROOT)

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
