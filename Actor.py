#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sqlite3
import os

db_path = ""
out_path = ""
db_tablename_actor = "actor"
db_tablename_moves = "movie"
db = None
search_actor_name = ""

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
    db = sqlite3.connect(db_path)
    db.execute('''CREATE TABLE IF NOT EXISTS actor (
        actor_id varchar(64) primary key,
        actor_name text,
        actor_photo_url text
    )''')
    db.execute('''CREATE TABLE IF NOT EXISTS movie (
        movie_id varchar(64) primary key,
        movie_name text,
        movie_actors text,
        movie_main_photo text,
        movie_photos text,
        movie_download_urls text
    ) ''')
    db.commit()

def start_anlyze():
    "Analyze Actor"
    pass

if __name__ == "__main__":
    print "main"
    load_config()
    init_db()

