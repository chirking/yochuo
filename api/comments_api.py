#!/usr/bin/env python
#coding=utf-8

import pymongo
from mongo import db
from datetime import datetime
import idautoincrement

def add_media_comments(media_id, media_user_id, user_id, content):
	comment = {'id':idautoincrement.get_id('comment'),'media_id':media_id,'media_user_id':media_user_id,'user_id':user_id,'content':content,'time':datetime.utcnow()}
	db.comment.save(comment)

	db.usernum.update({'user_id':user_id}, {'$inc':{'new_comment':1}}, False, False)
	db.media.update({'id':media_id}, {'$inc':{'comment_num':1}}, False, False)

	return comment


def get_media_comments(media_id):
	comments = db.comment.find({'media_id':media_id}).sort('time',pymongo.DESCENDING)
	return comments

def get_media_comments_by_id(id):
	commet = db.commemt.find_one({'id':id})
	return comment

def del_media_comments(id):
	db.comment.remove({'id':id})

	db.media.update({'id':id}, {'$inc':{'comment_num':-1}}, False, False)
