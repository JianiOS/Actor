#!/usr/bin/python
# -*- coding: UTF-8 -*-


class download_state(object):
    "Down load State"
    not_begin = 0
    error = 1
    downloading = 2
    success = 3
    failed = 4
    