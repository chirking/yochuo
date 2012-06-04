#!/usr/bin/env python
#coding=utf-8

from mongo import db
from datetime import datetime
import idautoincrement

import constant

radius = constant.radius

def add_locations(latitude, longitude, name):
	location = {'id':idautoincrement.get_id('location'),'name':name, 'loc':[latitude, longitude],'time':datetime.utcnow()}
	db.location.save(location)
	return location

def get_locations(id):
	location = db.location.find({'id':id})
	return location

def get_locations_search(latitude, longitude, min_id, max_id, count):
	location_find = {'loc':{"$within": {"$center": [[latitude, longitude], radius]}}}
	if (min_id is not None):
		location_find['id'] = {'$gte':min_id}
	if (max_id is not None):
		location_find['id'] = {'$lt':max_id}
	locations = db.location.find(location_find).limit(count)
	return locations

def get_locations_media(location_id):
	medias = db.media.find({'location_id':location_id, 'status':1})
	return medias

