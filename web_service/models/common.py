import os
import sys

SERVER_OK = 200

SERVER_ERROR = 500

NOT_FOUND = 404

INSERT_TRANSACTION_JSON_SCHEMA = {
									"type": "object",
									"required": ["type", "amount"],
									"properties" : {
										"transaction_id": {"type": "number"},
										"type": {"type": "string"},
										"amount": {"type": "number"},
										"parent_id": {"type": "number"}
									}
								}