import os
import sys

from models.base_test import BaseTest

class TypeAPI(BaseTest):
	def __init__(self, host, user_name=None, password=None):
		super(TypeAPI, self).__init__(host, user_name, password)
		
	def retrieve(self, type):
		return self.get('/transactionservice/type/{0}'.format(type))
		
if __name__ == '__main__':
	api = TypeAPI('http://127.0.0.1:5000', 'admin', 'Welcome123')
	print api.retrieve("TEST")