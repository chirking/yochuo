#!/usr/bin/env python
#coding=utf-8

import pymongo
from mongo import db
from datetime import datetime
import idautoincrement
import constant

radius = constant.radius

def get_media_recent(latitude, longitude, min_id, max_id, count):
	media_find = {'status':1, 'loc':{"$within": {"$center": [[latitude, longitude], radius]}}}
	if (min_id is not None):
		media_find['id'] = {'$gte':min_id}
	if (max_id is not None):
		media_find['id'] = {'$lt':max_id}
	medias = db.media.find(media_find).sort('time',pymongo.DESCENDING).limit(count)
	return medias