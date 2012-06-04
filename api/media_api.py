#!/usr/bin/env python
#coding=utf-8

import pymongo
from mongo import db
from datetime import datetime
import idautoincrement

def add_image(user_id, info, latitude, longitude, location_id, location_name, person):
	media = {'id':idautoincrement.get_id('media'),'type':'image','user_id':user_id,'info':info,'loc':[latitude, longitude],'location_id':location_id,'location_name':location_name,'person':person,'status':0,'comment_num':0,'like_num':0,'notice_status':0,'time':datetime.utcnow()}
	db.media.save(media)

	db.usernum.update({'user_id':user_id}, {'$inc':{'media':1}}, False, False)

	return media

def put_url(id, url):
	db.media.update({'id':id}, {'$set':{'url':url,'status':1}}, False, False)

def get_media(id):
	media = db.media.find_one({'id':id})
	return media


def get_medias(ids):
	medias = db.media.find({'id':{'$in':ids}}).sort('time',pymongo.DESCENDING)
	return medias

def del_media(id):
	db.media.remove({'id':id})

	db.usernum.update({'user_id':user_id}, {'$inc':{'media':-1}}, False, False)


def get_users_medias(user_id):
	medias = db.media.find({'user_id':user_id, 'status':1}).sort('time',pymongo.DESCENDING)
	return medias




