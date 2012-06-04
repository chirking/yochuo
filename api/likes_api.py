#!/usr/bin/env python
#coding=utf-8

import pymongo
from mongo import db
from datetime import datetime
import idautoincrement

def add_media_likes(media_id, media_user_id, user_id):
	like = {'id':idautoincrement.get_id('like'),'media_id':media_id,'media_user_id':media_user_id,'user_id':user_id,'time':datetime.utcnow()}
	db.like.save(like)

	db.media.update({'media_id':media_id}, {'$inc':{'like_num':1}}, False, False)

	return like


def get_media_likes(media_id):
	likes = db.like.find({'media_id':media_id}).sort('time',pymongo.DESCENDING)
	return likes

def get_users_likes_media(user_id):
	likes = db.like.find({'user_id':user_id}).sort('time',pymongo.DESCENDING)
	if likes.count() == 0:
		return None 
	media_ids = []
	for like in likes:
		media_ids.append(like['media_id'])
	medias = db.media.find({'id':{'$in':media_ids}}).sort('time',pymongo.DESCENDING)
	return medias

def del_media_likes(media_id, user_id):
	db.like.remove({'media_id':media_id, 'user_id':user_id})

	db.media.update({'media_id':media_id}, {'$inc':{'like_num':-1}}, False, False)