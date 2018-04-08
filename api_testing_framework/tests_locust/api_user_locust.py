import os
import sys

from locust import HttpLocust, TaskSet, task

sys.path.append('.')

from library.n26_api_models.transaction import TransactionAPI
from library.n26_api_models.type import TypeAPI
from library.n26_api_models.sum import SumAPI

class APIBehavior(TaskSet):
	def on_start(self):
		pass
	
	def on_stop(self):
		pass
	
	@task(1)
	def get_transaction(self):
		api = TransactionAPI('http://127.0.0.1:5000', 'admin', 'Welcome123')
		api.retrieve(1)
	
	@task(2)
	def get_sum(self):
		api = SumAPI('http://127.0.0.1:5000', 'admin', 'Welcome123')
		api.sum(1)
	
	@task(3)
	def get_type(self):
		api = TypeAPI('http://127.0.0.1:5000', 'admin', 'Welcome123')
		api.retrieve("TEST")
		
class APIUser(HttpLocust):
	task_set = APIBehavior
	min_wait = 1000
	max_wait = 2000