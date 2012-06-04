#!/usr/bin/env python
#coding=utf-8

import os
import sys

api_dir = os.path.abspath('../api')
sys.path.append(api_dir)

import users_api

import simplejson as json
import jsoncreater

def test_add_users():
	email = 'aaa@111.com'
	password = 'hello1234'
	nick = 'nick1'
	photo_url = 'a.a'
	about = u'没什么'
	openID_uid = u'微博1'
	openID_source = 'sina'
	user = users_api.add_users(email, password, nick, photo_url, about, openID_uid, openID_source)
	print user

def test_add_openID():
	user_id = 8
	openID_uid = u'微博2'
	openID_source = 'qq'

	users_api.add_openID(user_id, openID_uid, openID_source)

def test_get_openIDs():
	user_id = 8

	openIDs = users_api.get_openIDs(user_id)
	print openIDs[0]

def test_get_user():
	id = ''
	user = users_api.get_user(id)
	print user

def test_get_users():
	ids = [1,2,3,4,5,6,7,8]
	users = users_api.get_users(ids)
	print users[0]
	print jsoncreater.json_user(users[0])

def test_login():
	email = 'aaa@111.com'
	password = 'hello1234'
	user = users_api.login(email, password)
	print user

def test_login_by_openID():
	openID_uid= u'微博1'
	openID_source = 'sina'
	user = users_api.login_by_openID(openID_uid, openID_source)
	print user

def test_clear_notice():
	user_id = ''
	
	users_api.clear_notice(user_id)


if __name__ == '__main__':
	#test_add_users()
	#test_login()
	#test_login_by_openID()
	#test_add_openID()
	test_get_users()
	#test_get_openIDs()

