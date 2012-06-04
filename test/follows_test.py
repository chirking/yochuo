#!/usr/bin/env python
#coding=utf-8

import os
import sys

api_dir = os.path.abspath('../api')
sys.path.append(api_dir)

import follows_api

def test_add_users_follows():
	user_id = 8
	following = 7

	#user_id = 6
	#following = 8	

	follow = follows_api.add_users_follows(user_id, following)

	print follow

def test_get_users_followings():
	user_id = 8
	followings = follows_api.get_users_followings(user_id)
	print followings[0]

def test_get_users_followers():
	user_id = 7
	followers = follows_api.get_users_followers(user_id)
	print followers[0]

def test_del_users_followings():
	user_id = 8
	following = 7
	follows_api.del_users_followings(user_id, following)


def test_del_users_followers():
	user_id = 6
	follower = 8
	follows_api.del_users_followers(user_id, follower)


if __name__ == '__main__':
	#test_add_users_follows()
	test_get_users_followers()
	test_get_users_followings()
	test_del_users_followers()
	test_del_users_followings()