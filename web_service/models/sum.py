import os
import sys
import logging

from flask.views import MethodView
from flask import make_response, jsonify
from models.singleton_db import SingletonDB
from common import SERVER_OK

logger = logging.getLogger("n26.sum")

class SumAPI(MethodView):
	def get(self, transaction_id):
		db = SingletonDB()
		response = {"sum": 0}
		statement = """SELECT SUM(COALESCE(amount, 0)) FROM 
					transactions WHERE parent_id={0}
					GROUP BY parent_id""".format(transaction_id)
		logger.debug(statement)
		row = next(db.get(statement), None)
		if row:
			response["sum"] = row[0]
		return make_response(jsonify(response), SERVER_OK)