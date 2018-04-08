import os
import sys

from library.n26_api_models.base_test import BaseTest

class TransactionAPI(BaseTest):
	def __init__(self, host, user_name=None, password=None):
		super(TransactionAPI, self).__init__(host, user_name, password)
		
	def retrieve(self, transaction_id):
		return self.get('/transactionservice/transaction/{0}'.format(transaction_id))
		
	def insert(self, transaction_id, **kwargs):
		return self.put('/transactionservice/transaction/{0}'.format(transaction_id), **kwargs)
		
		
if __name__ == '__main__':
	api = TransactionAPI('http://127.0.0.1:5000', 'admin', 'Welcome123')
	print api.retrieve(1)
	print api.insert(1)