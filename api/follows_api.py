#!/usr/bin/env python
#coding=utf-8

import pymongo
from mongo import db
from datetime import datetime
import idautoincrement

def add_users_follows(user_id, following):
	follow = {'id':idautoincrement.get_id('follow'),'follower':user_id,'following':following,'time':datetime.utcnow()}
	db.follow.save(follow)

	db.usernum.update({'user_id':user_id}, {'$inc':{'following':1}}, False, False)

	return follow

def get_users_followings(user_id):
	followings = db.follow.find({'follower':user_id}).sort('time',pymongo.DESCENDING)
	if followings.count() == 0:
		return None 
	user_ids = []
	for following in followings:
		user_ids.append(like['followering'])
	users = db.media.find({'id':{'$in':user_ids}}).sort('time',pymongo.DESCENDING)
	return users

def get_users_followers(user_id):
	followers = db.follow.find({'following':user_id}).sort('time',pymongo.DESCENDING)
	if followers.count() == 0:
		return None 
	user_ids = []
	for follower in followers:
		user_ids.append(like['follower'])
	users = db.media.find({'id':{'$in':user_ids}}).sort('time',pymongo.DESCENDING)
	return users

def del_users_followings(user_id, following):
	db.follow.remove({'follower':user_id,'following':following})

	db.usernum.update({'user_id':user_id}, {'$inc':{'following':-1}}, False, False)
	db.usernum.update({'user_id':following}, {'$inc':{'follower':-1}}, False, False)


def del_users_followers(user_id, follower):
	db.follow.remove({'following':user_id,'follower':follower})

	db.usernum.update({'user_id':user_id}, {'$inc':{'follower':-1}}, False, False)
	db.usernum.update({'user_id':follower}, {'$inc':{'following':-1}}, False, False)