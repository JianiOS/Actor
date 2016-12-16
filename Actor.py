#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sqlite3
import os

db_path = ""
out_path = ""

db = None

def run():
    "Run"
    print "Run"
    return None

def load_config():
    "Load Default Config"
    global db_path
    global out_path

    downlaod_path = os.getcwd() + "/Download/"
    if not os.path.exists(downlaod_path):
        os.makedirs(downlaod_path)
    if len(db_path) == 0:
        db_path = os.getcwd() + "/Download/data.db"
    if len(out_path) == 0:
        out_path = os.getcwd() + "/Download"

def init_db():
    "DB init"
    global db

if __name__ == "__main__":
    print "main"
    run()
    load_config()

