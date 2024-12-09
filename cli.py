#!/usr/bin/env python3
#-*- coding: utf-8 -*-
"""
@author: eze-root
@file: cli.py
@time: 2024/12/07
"""

import os
import logging
import datetime
import argparse
import subprocess

from collections import defaultdict
from typing import Tuple


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')
DRAFT_DIR = os.path.join(BASE_DIR, 'source', 'drafts')

today = datetime.datetime.now().strftime("%Y-%m-%d")
parser = argparse.ArgumentParser()
parser.add_argument("--dirpath", default=BASE_DIR, help="Current Dir")
parser.add_argument(
    "--add_draft", default=today, help="Your Draft Name, please end with .md"
)
args = parser.parse_args()


logger = logging.getLogger(__name__)
logging.basicConfig(format="%(message)s", level=logging.DEBUG)


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
    return user_name.strip(), user_email.strip()


def add_a_draft():
    draft_fpath = os.path.join(TEMPLATE_DIR, 'article.md')
    output_fpath = os.path.join(DRAFT_DIR, args.add_draft)
    if not output_fpath.endswith('.md'):
        output_fpath = f'{output_fpath}.md'
    user_name, user_email = get_local_github_account_info()
    with open(draft_fpath) as f:
        content = f.read()
    content = content.replace('##user_name##', user_name)
    with open(output_fpath, 'w') as f:
        f.write(content)
    logger.info(f'{user_name} write an article in {output_fpath}')
    logger.info(f'Just open {output_fpath} to write your content!!')


def main():
    add_a_draft()

if __name__ == "__main__":
    main()
