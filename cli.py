#!/usr/bin/env python3
#-*- coding: utf-8 -*-
"""
@author: eze-root
@file: cli.py
@time: 2024/12/07
"""

import os
import re
import sys
import time
import json
import math
import random
import pickle
import logging
import argparse
import subprocess

from collections import defaultdict
from typing import Tuple


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DRAFT_DIR = os.path.join(BASE_DIR, 'templates')

parser = argparse.ArgumentParser()
parser.add_argument('--dirpath', default=BASE_DIR, help='Current Dir')
parser.add_argument('--add_draft', default=BASE_DIR, help='Your Draft Name')
args = parser.parse_args()

def get_local_github_account_info() -> Tuple[str, str]:
    """
    Get Local Github Account Info
    """
    user_name_cmdline = 'git config user.name'
    user_email_cmdline = 'git config user.email'
    output = subprocess.run(user_name_cmdline, shell=True, capture_output=True)
    user_name = output.stdout.decode('utf8')

    output = subprocess.run(user_email_cmdline, shell=True, capture_output=True)
    user_email = output.stdout.decode('utf8')
    return user_name, user_email


def add_a_draft():
    draft_fpath = os.path.join(DRAFT_DIR, 'draft.md')

    pass


def main():
    pass

if __name__ == "__main__":
    main()
