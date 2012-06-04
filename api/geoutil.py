#!/usr/bin/env python
#coding=utf-8

unit = 6371000.0

def get_radius_by_meter(meter):
	return meter/unit

def get_meter_by_radius(radius):
	return radius*unit

def get_meter():
	pass