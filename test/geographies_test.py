#!/usr/bin/env python
#coding=utf-8

import os
import sys

api_dir = os.path.abspath('../api')
sys.path.append(api_dir)

import geographies_api

def test_get_media_recent():
	latitude = 2.12345678
	longitude = 2.12345678
	min_id = None 
	max_id = None 
	count = 10
	medias = geographies_api.get_media_recent(latitude, longitude, min_id, max_id, count)
	print medias[0]

if __name__ == '__main__':
	test_get_media_recent()