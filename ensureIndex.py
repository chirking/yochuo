#!/usr/bin/env python
#coding=utf-8

import os
import sys

api_dir = os.path.abspath('api')
sys.path.append(api_dir)

from mongo import db
import pymongo


db.location.ensure_index([('loc', pymongo.GEO2D)])
db.media.ensure_index([('loc', pymongo.GEO2D)])

db.user.ensure_index([('id', pymongo.DESCENDING)])
db.follow.ensure_index([('id', pymongo.DESCENDING)])
db.media.ensure_index([('id', pymongo.DESCENDING)])
db.like.ensure_index([('id', pymongo.DESCENDING)])
db.comment.ensure_index([('id', pymongo.DESCENDING)])
db.message.ensure_index([('id', pymongo.DESCENDING)])

db.user.ensure_index([('user_id', pymongo.DESCENDING)])
db.follow.ensure_index([('user_id', pymongo.DESCENDING)])
db.media.ensure_index([('user_id', pymongo.DESCENDING)])
db.like.ensure_index([('user_id', pymongo.DESCENDING)])
db.like.ensure_index([('media_id', pymongo.DESCENDING)])
db.comment.ensure_index([('user_id', pymongo.DESCENDING)])
db.comment.ensure_index([('media_id', pymongo.DESCENDING)])
db.message.ensure_index([('user_id', pymongo.DESCENDING)])
db.usernum.ensure_index([('user_id', pymongo.DESCENDING)])

print 'OK!'

db.idautoincrement.update({'key':'user'}, {"$inc":{"value":1}}, True, False)
db.idautoincrement.update({'key':'follow'}, {"$inc":{"value":1}}, True, False)
db.idautoincrement.update({'key':'media'}, {"$inc":{"value":1}}, True, False)
db.idautoincrement.update({'key':'like'}, {"$inc":{"value":1}}, True, False)
db.idautoincrement.update({'key':'comment'}, {"$inc":{"value":1}}, True, False)
db.idautoincrement.update({'key':'message'}, {"$inc":{"value":1}}, True, False)
db.idautoincrement.update({'key':'usernum'}, {"$inc":{"value":1}}, True, False)
db.idautoincrement.update({'key':'location'}, {"$inc":{"value":1}}, True, False)

