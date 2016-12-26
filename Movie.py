#!/usr/bin/python
# -*- coding: UTF-8 -*-

from download_state import download_state

class actor(object):
    "Class Actor"

    def __init__(self, name):
        self.name = name
        self.actor_id = ""
        self.thumb_url = ""


class movie(object):
    "Class Movie"

    def __init__(self):
        self.movie_id = ""
        self.title = ""
        self.actors = []
        self.cover_photo = ""
        self.thumbs = []
        self.download_urls = []
        self.state = download_state.not_begin
        self.href = ""
    def __repr__(self):
        return "{} {} {} {}\n".format(self.movie_id, self.title, self.href, self.download_urls)
        