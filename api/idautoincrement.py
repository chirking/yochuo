#!/usr/bin/env python
#coding=utf-8

from mongo import db
from datetime import datetime

def get_id(key):
	id = db.idautoincrement.find_and_modify({'key':key}, {"$inc":{"value":1}}, False).get('value')
	return id