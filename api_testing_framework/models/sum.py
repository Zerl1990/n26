import os
import sys

from models.base_test import BaseTest

class SumAPI(BaseTest):
	def __init__(self, host, user_name=None, password=None):
		super(SumAPI, self).__init__(host, user_name, password)
		
	def sum(self, transaction_id):
		return self.get('/transactionservice/sum/{0}'.format(transaction_id))
		
if __name__ == '__main__':
	api = SumAPI('http://127.0.0.1:5000', 'admin', 'Welcome123')
	print api.sum(1)