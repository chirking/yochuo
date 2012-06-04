# Create your models here.

from mongoengine import *
import datetime

class User(Document):
  email = StringField(required=True)
  password = StringField(required=True)
  petName = StringField()
  photoUrl = StringField()
  about = StringField()
  openId = ListField(ObjectIdField())
  createTime = DateTimeField(default=datetime.datetime.now)

class Num(Document):
  following = IntField()
  follower = IntField() 
  like = IntField() 
  newComment = IntField()
  newMessage = IntField()

class follow(Document):
  followerUserId = ObjectIdField()
  followingUserId = ObjectIdField()
  time = DateTimeField(default=datetime.datetime.now) 


class OpenId(Document):
  userId = ObjectIdField()
  source = StringField()
  uid = StringField()

class media(Document):
  url = StringField()
  userId = ObjectIdField()
  addressId = ObjectIdField() 
  addressName = StringField()
  person = ListField(ObjectIdField())
  about = StringField()
  geohash = StringField()
  latitude = FloatField()
  longitude = FloatField()
  likeNum = IntField()
  time = DateTimeField(default=datetime.datetime.now)
  noticeStatus = IntField()

class inbox(Document):
  userId = ObjectIdField()
  picId = ObjectIdField()
  ownUserId = ObjectIdField()
  time = DateTimeField(default=datetime.datetime.now) 

class like(Document):
  userId = ObjectIdField()
  picId = ObjectIdField()
  ownUserId = ObjectIdField()
  time = DateTimeField(default=datetime.datetime.now) 
  create_time = DateTimeField(default=datetime.datetime.now)

class comment(Document):
  picId = ObjectIdField()
  picUserId = ObjectIdField()
  userId = ObjectIdField()
  content = StringField() 
  createTime = DateTimeField(default=datetime.datetime.now)

class Address(Document):
  name = StringField() 
  geohash = StringField()
  latitude = FloatField()
  longitude = FloatField()
  useNum = IntField()
  createTime = DateTimeField(default=datetime.datetime.now)

class Message(Document):
  sendUserId = ObjectIdField()
  receiveUserId = ObjectIdField()
  content = StringField()
  createTime = DateTimeField(default=datetime.datetime.now)

