#!/usr/bin/env python
#coding=utf-8

import os
import sys

api_dir = os.path.abspath('../api')
sys.path.append(api_dir)

import media_api

def test_add_image():
	user_id = 8
	info = u'我在这里'
	latitude = 2.12345678
	longitude = 2.12345678
	location_id = 1
	location_name = u'有树' 
	person = None

	media = media_api.add_image(user_id, info, latitude, longitude, location_id, location_name, person)
	print media

def test_put_url():
	id = 1
	url = 'www.aaa.pic'
	media_api.put_url(id, url)

def test_get_media():
	id = 1
	media = media_api.get_media(id)
	print media


def test_get_medias():
	ids = [1,2,3]
	medias = media_api.get_medias(ids)
	print medias[0]

def test_del_media(id):
	id = 1
	media_api.remove(id)


def test_get_users_medias():
	user_id = 8
	medias = media_api.get_users_medias(user_id)
	print medias[0]


if __name__ == '__main__':
	#test_add_image()
	#test_get_medias()
	#test_put_url()
	test_get_users_medias()



