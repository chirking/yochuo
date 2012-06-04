#!/usr/bin/env python
#coding=utf-8

import os
import sys

api_dir = os.path.abspath('../api')
sys.path.append(api_dir)

import locations_api
from mongo import db

def test_add_locations():
	latitude = 2.12345678
	longitude = 2.12345678
	name = u'有树' 

	location = locations_api.add_locations(latitude, longitude, name)
	print location

def test_get_locations_search():
	latitude = 2.12345678
	longitude = 2.12345678
	min_id = None 
	max_id = None 
	count = 10
	locations = locations_api.get_locations_search(latitude, longitude, min_id, max_id, count)
	
	print locations[0]


def test_get_locations_media():
	location_id = 1
	medias = locations_api.get_locations_media(location_id)
	print medias[0]


if __name__ == '__main__':
	#from bson.son import SON
	#result = db.command(SON([('geoNear', 'location'), ('near', [2.12345678, 2.12345678])]))
	#print result
	#print result['stats']
	#import constant
	#print constant.radius


	#test_add_locations()
	
	test_get_locations_search()
	test_get_locations_media()

