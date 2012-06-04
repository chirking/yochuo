#!/usr/bin/env python
#coding=utf-8

from tornado.web import RequestHandler
import users_api
import media_api
import likes_api
import comments_api

class MediaHandler(RequestHandler):
	"""docstring for user"""
	def get(self):
		media_id = self.request.arguments['media_id']
		media = media_api.get_media(id)

	def put(self):
		user_id = self.request.arguments['user_id']
		info = self.request.arguments['info']
		latitude = self.request.arguments['latitude']
		longitude = self.request.arguments['longitude']
		location_id = self.request.arguments['location_id']
		location_name = self.request.arguments['location_name']
		person = self.request.arguments['person']

		media = media_api.add_image(user_id, info, latitude, longitude, location_id, location_name, person)

	def delete(self):
		pass


class LikesHandler(RequestHandler):
	"""docstring for Likes"""
	def get(self):
		media_id = self.request.arguments['media_id']
		likes = likes_api.get_media_likes(media_id)

	def put(self):
		media_id = self.request.arguments['media_id']
		media_user_id = self.request.arguments['media_user_id']
		user_id = self.request.arguments['user_id']

		like = likes_api.add_media_likes(media_id, media_user_id, user_id)

	def delete(self):
		user_id = self.request.arguments['user_id']
		media_id = self.request.arguments['media_id']

		likes_api.del_media_likes(media_id, user_id)


class CommentsHandler(RequestHandler):
	"""docstring for ClassName"""
	def get(self):
		media_id = self.request.arguments['media_id']
		comments = comments_api.get_media_comments(media_id)

	def put(self):
		media_id = self.request.arguments['media_id']
		media_user_id = self.request.arguments['media_user_id']
		user_id = self.request.arguments['user_id']

		comment = comments_api.add_media_comments(media_id, media_user_id, user_id)

	def delete(self):
		comment_id = self.request.arguments['comment_id']

		comments_api.del_media_comments(comment_id)
		


		