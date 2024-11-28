#!/usr/bin/env python3
#-*- coding: utf-8 -*-
"""
@author: eze-root
@file: cli.py
@time: 2024/11/27
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

parser = argparse.ArgumentParser()
parser.add_argument('--dirpath', default=BASE_DIR, help='Current Dir')
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


def main():
    user_name, user_email = get_local_github_account_info()



if __name__ == "__main__":
    main()


