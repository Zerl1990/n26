import os
import sys


from library.n26_api_models.transaction import TransactionAPI
from library.n26_api_models.type import TypeAPI
from library.n26_api_models.sum import SumAPI

__version__ = '0.1'

class N26Library(object):
	def __init__(self, host, user, password):
		self.host = host
		self.user = user
		self.password = password

	def add_new_transaction(self, transaction_id, type, amount, parent_id=None):
		api = TransactionAPI(self.host, self.user, self.password)
		args = {"type": type, "amount": amount}
		if parent_id:
			args["parent_id"] = parent_id
		return api.insert(transaction_id, **args)
	
	def get_transaction_by_id(self, transaction_id):
		api = TransactionAPI(self.host, self.user, self.password)
		return api.retrieve(transaction_id)

	def get_transaction_sum(self, transaction_id):
		api = SumAPI(self.host, self.user, self.password)
		return api.sum(transaction_id)

	def get_transactions_by_type(self, type):
		api = TypeAPI(self.host, self.user, self.password)
		return api.retrieve(type)