#!/usr/bin/env python
#coding=utf-8

import os
import sys

api_dir = os.path.abspath('../api')
sys.path.append(api_dir)

import likes_api

def test_add_media_likes():
	media_id = 1
	media_user_id = 8
	user_id = 7

	like = likes_api.add_media_likes(media_id, media_user_id, user_id)

	print like


def test_get_media_likes():
	media_id = 1
	likes = likes_api.get_media_likes(media_id)
	print likes[0]

def test_get_media_likes_by_id():
	id = 1
	commet = likes_api.get_media_likes_by_id(id)
	print like

def test_del_media_likes():
	media_id = 1
	user_id = 7
	likes_api.del_media_likes(media_id, user_id)

def test_get_users_likes_media():
	user_id = 7
	medias = likes_api.get_users_likes_media(user_id)
	print medias[0]


if __name__ == '__main__':
	#test_add_media_likes()
	test_get_media_likes()
	#test_del_media_likes()
	test_get_users_likes_media()