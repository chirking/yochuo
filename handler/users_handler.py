#!/usr/bin/env python
#coding=utf-8

from tornado.web import RequestHandler
import users_api
import media_api
import likes_api
import follow_api

class UserHandler(RequestHandler):
	"""docstring for user"""
	def get(self):
		user_id = self.request.arguments['user_id']
		user = users_api.get_user(user_id)
		usernum = users_api.get_usernum(user_id)

	def put(self):
		email = self.request.arguments['email']
		password = self.request.arguments['password']
		nick = self.request.arguments['nick']
		photo_url = self.request.arguments['photo_url']
		about = self.request.arguments['about']
		openID_uid = self.request.arguments['openID_uid']
		openID_source = self.request.arguments['openID_source']
		
		user = users_api.add_users(email, password, nick, photo_url, about, openID_uid, openID_source)
		

class MediaHandler(RequestHandler):
	"""docstring for mediaHandler"""
	def get(self):
		user_id = self.request.arguments['user_id']
		medias = media_api.get_users_medias(user_id)
		

class MediaLikedHandler(RequestHandler):
	"""docstring for mediaHandler"""
	def get(self):
		user_id = self.request.arguments['user_id']
		medias = likes_api.get_users_likes_media(user_id)


class FollowerHandler(RequestHandler):
	"""docstring for FollowerHandler"""
	def get(self):
		user_id = self.request.arguments['user_id']
		followers = follow_api.get_users_followers(user_id)

	def delete(self):
		user_id = self.request.arguments['user_id']
		follower = self.request.arguments['follower']
		follow_api.del_users_followers(user_id, follower)


class FollowingHandler(RequestHandler):
	"""docstring for ClassName"""
	def get(self):
		user_id = self.request.arguments['user_id']
		followings = follow_api.get_users_followings(user_id)

	def put(self):
		user_id = self.request.arguments['user_id']
    	following = self.request.arguments['following']
		follows_api.add_users_follows(user_id, following)

	def delete(self):
		user_id = self.request.arguments['user_id']
		following = self.request.arguments['following']
		follow_api.del_users_followings(user_id, following)

		

		


		