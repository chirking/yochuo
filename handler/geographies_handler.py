#!/usr/bin/env python
#coding=utf-8

from tornado.web import RequestHandler
import users_api
import media_api
import locations_api

class MediaRecentHandler(RequestHandler):
	def get(slef):
		latitude = self.request.arguments['latitude']
		longitude = self.request.arguments['longitude']
		min_id = self.request.arguments['min_id'] 
		max_id = self.request.arguments['max_id'] 
		count = self.request.arguments['count']

		medias = geographies_api.get_media_recent(latitude, longitude, min_id, max_id, count)
