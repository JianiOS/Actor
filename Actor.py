#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sqlite3
import os
import Analyze

SEARCH_URL = "https://www.javbus.info/search/"
MAIN_PATH = "https://www.javbus.info"

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
        actor_thumb_url text
    )''')
    db.execute('''CREATE TABLE IF NOT EXISTS movie (
        movie_id varchar(64) primary key,
        movie_title text,
        movie_actors text,
        movie_cover_photo text,
        movie_thumbs text,
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

    def callback(state, movies):
        if state == Analyze.download_state.success:
            print movies
        else:
            pass
    Analyze.analyze_list_path(callback, path="https://www.javbus.info")
