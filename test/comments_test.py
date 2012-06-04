#!/usr/bin/env python
#coding=utf-8

import os
import sys

api_dir = os.path.abspath('../api')
sys.path.append(api_dir)

import comments_api

def test_add_media_comments():
	media_id = 1
	media_user_id = 8
	user_id = 7
	content = u'非常漂亮'

	comment = comments_api.add_media_comments(media_id, media_user_id, user_id, content)

	print comment


def test_get_media_comments():
	media_id = 1
	comments = comments_api.get_media_comments(media_id)
	print comments[0]

def test_get_media_comments_by_id():
	id = 0
	commet = comments_api.get_media_comments_by_id()
	print comment

def test_del_media_comments():
	id = 1
	comments_api.del_media_comments(id)


if __name__ == '__main__':
	#test_add_media_comments()
	#test_get_media_comments()
	test_del_media_comments()