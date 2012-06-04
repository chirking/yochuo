#!/usr/bin/env python
#coding=utf-8

import pymongo
from mongo import db
from datetime import datetime
import idautoincrement

def add_users(email, password, nick, photo_url, about, openID_uid, openID_source):
	user = {'id':idautoincrement.get_id('user'),'email':email,'password':password,'nick':nick,'photo_url':photo_url,'about':about,'time':datetime.utcnow()}
	db.user.save(user)

	db.usernum.save({'user_id':user['id'], 'following':0, 'follower':0, 'media':0, 'new_follower':0, 'new_comment':0, 'new_message':0})

	if (openID_uid is not None):
		openID = {'user_id':user['id'],'openID_uid':openID_uid,'openID_source':openID_source,'type':'create','time':datetime.utcnow()}
		db.openID.save(openID)
	return user

def add_openID(user_id, openID_uid, openID_source):
	openID = {'openID_uid':openID_uid,'openID_source':openID_source,'type':'create','time':datetime.utcnow()}
	db.openID.save(openID)
	return openID

def get_openIDs(user_id):
	openIDs = db.openID.find({'user_id':user_id})
	return openIDs

def get_user(id):
	user = db.user.find_one({'id':id})
	return user

def get_users(ids):
	users = db.user.find({'id':{'$in':ids}}).sort('time',pymongo.DESCENDING)
	return users

def get_usernum(user_id):
	usernum = db.usernum.find_one({'user_id':user_id})
	return usernum

def login(email, password):
	user = db.user.find_one({'email':email})
	if (user is None):
		return None
	if (user['password'] != password):
		return None
	return user

def login_by_openID(openID_uid, openID_source):
	openID_find = {'openID_uid':openID_uid,'openID_source':openID_source}
	openID = db.openID.find_one(openID_find)
	if (openID is None):
		return None
	user_find = {'id':openID['user_id']}
	user = db.user.find_one(user_find)
	return user

def clear_notice(user_id):
	db.user.update({'user_id':user_id},{'$set':{'new_follower':0, 'new_comment':0, 'new_message':0}}, False, True)

