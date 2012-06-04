#!/usr/bin/env python
#coding=utf-8

import pymongo

con = pymongo.connection.Connection('mongodb://root:hello1234@mongoc2.grandcloud.cn:10003/yochuo')
db = con.yochuo


if (__name__=="__main__"):
	abc={'name':'lzy'}
	db.test.save(abc)
	print db.test.find()[0]
	print abc
