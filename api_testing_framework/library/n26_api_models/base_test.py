import os
import sys
import requests

class BaseTest(object):
	def __init__(self, host, user_name, password):
		self.host = host
		self.user_name = user_name
		self.password = password
		
	def get(self, url, query_params=None):
		url = self.host + url
		req = requests.get(url, auth=(self.user_name, self.password), params=query_params)
		return (req.status_code, req.json())
		
		
	def put(self, url, **kwargs):
		url = self.host + url
		req = requests.put(url, auth=(self.user_name, self.password), json=kwargs)
		return (req.status_code, req.json())
		
	