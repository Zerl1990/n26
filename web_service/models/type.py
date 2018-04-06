import os
import sys
import logging

from flask.views import MethodView
from flask import make_response, jsonify
from models.singleton_db import SingletonDB
from common import SERVER_OK

logger = logging.getLogger("n26.type")

class TypeAPI(MethodView):
	def get(self, type):
		db = SingletonDB()
		response = []
		statement = """SELECT transaction_id FROM TRANSACTIONS
					WHERE type='{0}'""".format(type)
		logger.debug(statement)
		return make_response(jsonify([row[0] for row in db.get(statement)]), SERVER_OK)		