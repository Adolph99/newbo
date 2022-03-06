#**************************************************
# Based on:
# Source: https://github.com/anasty17/mirror-leech-telegram-bot/blob/master/update.py
#**************************************************

import logging
from os import path as ospath, environ
from subprocess import run as srun
from requests import get as rget

if ospath.exists('botlog.txt'):
    with open('log.txt', 'r+') as f:
        f.truncate(0)

CONFIG_FILE_URL = environ.get('CONFIG_FILE_URL')
try:
    if len(CONFIG_FILE_URL) == 0:
        raise TypeError
    try:
        res = rget(CONFIG_FILE_URL)
        if res.status_code == 200:
            with open('config.env', 'wb+') as f:
                f.write(res.content)
        else:
            logging.error(f"Failed to download config.env {res.status_code}")
    except Exception as e:
        logging.error(f"CONFIG_FILE_URL: {e}")
except TypeError:
    logging.error(f"No data received...")
    pass

UPSTREAM_REPO = environ.get('UPSTREAM_REPO')
UPSTREAM_BRANCH = environ.get('UPSTREAM_BRANCH')
try:
    if len(UPSTREAM_REPO) == 0:
       raise TypeError
except TypeError:
    UPSTREAM_REPO = "https://github.com/Sam-Max/Rclone-Tg-Bot"

try:
    if len(UPSTREAM_BRANCH) == 0:
       raise TypeError
except TypeError:
    UPSTREAM_BRANCH = 'master'

if ospath.exists('.git'):
    srun(["rm", "-rf", ".git"])

srun([f"git init -q \
        && git config --global user.email sam.agd@outlook.com \
        && git config --global user.name rctgb \
        && git add . \
        && git commit -sm update -q \
        && git remote add origin {UPSTREAM_REPO} \
        && git fetch origin -q \
        && git reset --hard origin/{UPSTREAM_BRANCH} -q"], shell=True)