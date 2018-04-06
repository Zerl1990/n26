#!flask/bin/python
import os
import sys
import argparse
import logging
import traceback

from flaskext.auth import Auth
from flask import Flask, request, make_response, jsonify
from time import strftime

from models.common import SERVER_ERROR, NOT_FOUND
from models.transaction import TransactionAPI
from models.type import TypeAPI
from models.sum import SumAPI

# Create logger
logger = logging.getLogger("n26")

# Create flask app
app = Flask("n26")


# Create instances of models
transaction_view = TransactionAPI.as_view('transaction')
type_view = TypeAPI.as_view('type')
sum_view = SumAPI.as_view('sum')

# Define routes
app.add_url_rule('/transactionservice/transaction/<int:transction_id>', 
					view_func=transaction_view,
					methods=['GET', 'PUT'])	
app.add_url_rule('/transactionservice/type/<string:type>', 
					view_func=type_view,
					methods=['GET'])
app.add_url_rule('/transactionservice/sum/<int:transaction_id>', 
					view_func=sum_view,
					methods=['GET'])

# Just very basic authentication
@app.before_request
def before_request():
	auth = request.authorization
	if auth["username"] != "admin" or auth["password"] != "Welcome123":
		response = jsonify({"errror_msg": "Invalid User/Password"})
		return make_response(response, NOT_AUTH)
								
# Misc function to handle special cases
@app.after_request
def after_request(response):
	response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
	response.headers.add('Access-Control-Allow-Methods', 'GET, PUT, POST, DELETE, OPTIONS')
	return response

@app.errorhandler(Exception)
def exceptions(e):
	tb = traceback.format_exc()
	error_msg = "{0} {1} {2} {3} 5xx INTERNAL SERVER ERROR\n{4}".format(request.remote_addr, request.method,request.scheme, request.full_path, tb)
	logger.error(error_msg)
	response = jsonify({"errror_msg": error_msg})
	return make_response(response, SERVER_ERROR)
 
if __name__ == '__main__':
	#PORT
	DEFAULT_PORT = 5000
	
	# Parser
	parser = argparse.ArgumentParser()
	parser.add_argument("-d", help="Enable debug messages", action='store_true', default=False)
	parser.add_argument("--port", help="API Port", action='store', default=DEFAULT_PORT, type=int)
	parser.add_argument("--host", help="API Host", action='store', default='127.0.0.1')
	args = parser.parse_args()
	
	# Set logging level
	if args.d:
		app.logger.setLevel(logging.DEBUG)
	else:
		app.logger.setLevel(logging.ERROR)
	
	# Run application with file handler
	#app.run(host=args.host, port=args.port, debug=args.d, threaded=True, ssl_context='adhoc')
	app.run(host=args.host, port=args.port, debug=args.d, threaded=True)
