import os
import sys
import logging

from flask.views import MethodView
from flask import make_response, jsonify, request
from models.singleton_db import SingletonDB
from models.type import TypeAPI
from common import SERVER_OK, NOT_FOUND, INSERT_TRANSACTION_JSON_SCHEMA
from jsonschema import validate

logger = logging.getLogger("n26.transaction")

class TransactionAPI(MethodView):
	def get(self, transction_id):
		db = SingletonDB()
		response = None
		status_code = NOT_FOUND
		statement = """SELECT parent_id, type, amount FROM TRANSACTIONS
					WHERE transaction_id = {0}""".format(transction_id)
		logger.debug(statement)
		row = next(db.get(statement), None)
		if row:
			response = {"parent_id": row[0], "type": row[1], "amount": row[2]}
			status_code = SERVER_OK
		return make_response(jsonify(response), status_code)
			
			
		
	def put(self, transction_id):
		db = SingletonDB()
		post_content = request.get_json(force=True)
		post_content["transaction_id"] = transction_id
		validate(post_content, INSERT_TRANSACTION_JSON_SCHEMA)
		statement = """INSERT INTO TRANSACTIONS (TRANSACTION_ID, PARENT_ID, TYPE, AMOUNT)
		VALUES ({transaction_id}, {parent_id}, '{type}', {amount})""".format(**post_content)
		logger.debug(statement)
		db.insert(statement)
		return make_response("Transaction Added", SERVER_OK)