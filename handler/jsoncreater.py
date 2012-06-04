#!/usr/bin/env python
#coding=utf-8

import simplejson as json

def json_user(user):
	s = {'id':user['id'],'email':user['email'],'password':user['password'],'nick':user['nick'],'photo_url':user['photo_url'],'about':user['about']}
	return json.dumps(user)

def json_users(users):
	pass

def json_media(media):
	pass

def json_medias(medias):
	pass

def json_like(like):
	pass

def json_likes(likes):
	pass

def json_comment(comment):
	pass

def json_comments(comments):
	pass

def json_location(location):
	pass

def json_locations(locations):
	pass

