import os
import traceback
import logging
import threading
import sqlite3

logger = logging.getLogger("n26.singleton_db")

DB_CONNECT_STRING = 'models/sqlite3/n26.db'

class SingletonDB:
	class __DB():
		def __init__(self):
			self.conn = sqlite3.connect(DB_CONNECT_STRING, check_same_thread=False)
			
			
		def get(self, statement, **kwargs):
			return self.conn.execute(statement.format(**kwargs))
			
		def insert(self, statement, **kwargs):
			self.conn.execute(statement.format(**kwargs))
			self.conn.commit()
			
		def __del__(self):
			self.conn.close()
			
	__instance = None
	__lock = threading.RLock()
	
	def __init__(self):
		if SingletonDB.__instance is None:
			SingletonDB.__lock.acquire()
			SingletonDB.__instance = SingletonDB.__DB()
			self.__dict__['_SingletonDB__instance'] = SingletonDB.__instance
			SingletonDB.__lock.release()
			
	def __getattr__(self, attr):
		return getattr(self.__instance, attr)

	def __setattr__(self, attr, value):
		return setattr(self.__instance, attr, value)