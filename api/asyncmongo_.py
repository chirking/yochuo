#!/usr/bin/env python
#coding=utf-8

import asyncmongo

db = asyncmongo.Client(pool_id='mydb', host='mongoc2.grandcloud.cn', port=10003, maxcached=10, maxconnections=50, 
    dbname='yochuo', dbuser='root', dbpass='hello1234@')