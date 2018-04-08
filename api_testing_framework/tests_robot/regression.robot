*** Settings ***
Variables	../resources/env_vars.py
Library	library.n26_api_keywords.N26Library	${HOST}	${USER}	${PASS}
Library	Collections
Library	String

*** Test cases ***
Try To Get Not Existing Transaction
	${status}	${response}	Get Transaction By Id	0
	Should Be Equal As Integers	${status}	404
	
Try To Get Transaction Using String
	${status}	${response}	Get Transaction By Id	"something"
	Should Be Equal As Integers	${status}	500
	Dictionary Should Contain Key	${response}	error_msg
	
Try To Get Transaction With Empty Transaction ID
	${status}	${response}	Get Transaction By Id	None
	Should Be Equal As Integers	${status}	500
	Dictionary Should Contain Key	${response}	error_msg
	
Get Transactions By Type With Integer
	${status}	${response}	Get Transactions By Type	1234
	Should Be Equal As Integers	${status}	200
	Should Be Empty	${response}
	
Get Transactions By Type With Big String
	${status}	${response}	Get Transactions By Type	"String size greater than 255 character which is the max size for that column in the data base String size greater than 255 character which is the max size for that column in the data base String size greater than 255 character which is the max size for that column in the data base"
	Should Be Equal As Integers	${status}	200
	
Get Transactions By Type With Special Characters
	${status}	${response}	Get Transactions By Type	"5%$Q%$%$#@#@#^&$"
	Should Be Equal As Integers	${status}	200
	Should Be Empty	${response}
	
Try To Get Transaction Sum Of Not Existing Transaction ID
	${status}	${response}	Get Transaction Sum	0
	Should Be Equal As Integers	${status}	200
	Dictionary Should Contain Key	${response}	sum
	${sum}	Get From Dictionary	${response}	sum
	Should Be True	${sum} == 0
	
Try To Get Transaction Sum Of Transaction ID With String
	${status}	${response}	Get Transaction Sum	"%$Q%$#@%#@%@#%#@%@%#@$"
	Should Be Equal As Integers	${status}	200
	Dictionary Should Contain Key	${response}	sum
	${sum}	Get From Dictionary	${response}	sum
	Should Be True	${sum} == 0
	
Add New Transaction
	${random}	Evaluate    random.sample(range(1, 1000000), 1)    random
	${random}	Get From List	${random}	0
	${status}	${response}	Add New Transaction	${random}	"TEST"	${10}	${1}
	Should Be Equal As Integers	${status}	200
	
Add New Transaction With Big Amount
	${random}	Evaluate    random.sample(range(1, 1000000), 1)    random
	${random}	Get From List	${random}	0
	${status}	${response}	Add New Transaction	${random}	"TEST"	${1000000000000000}	${1}
	Should Be Equal As Integers	${status}	200
	
Add New Transaction With Small Amount
	${random}	Evaluate    random.sample(range(1, 1000000), 1)    random
	${random}	Get From List	${random}	0
	${status}	${response}	Add New Transaction	${random}	"TEST"	${0}	${1}
	Should Be Equal As Integers	${status}	200
	
Add New Transaction With Negative Amount
	${random}	Evaluate    random.sample(range(1, 1000000), 1)    random
	${random}	Get From List	${random}	0
	${status}	${response}	Add New Transaction	${random}	"TEST"	${-10}	${1}
	Should Be Equal As Integers	${status}	200
	
Add New Transaction With String Amount
	${random}	Evaluate    random.sample(range(1, 1000000), 1)    random
	${random}	Get From List	${random}	0
	${status}	${response}	Add New Transaction	${random}	"TEST"	"SFS#@$@"	${1}
	Should Be Equal As Integers	${status}	500
	
Add New Transaction With String ID
	${status}	${response}	Add New Transaction	"%$#@%#$#@"	"TEST"	${10}	${1}
	Should Be Equal As Integers	${status}	500
	
Add New Transactions Of New Type
	${random_type}	Generate Random String
	${random}	Evaluate    random.sample(range(1, 1000000), 1)    random
	${random}	Get From List	${random}	0
	${status}	${response}	Add New Transaction	${random}	${random_type}	${10}	${1}
	Should Be Equal As Integers	${status}	200
	${status}	${response}	Get Transactions By Type	${random_type}
	Should Be Equal As Integers	${status}	200
	Should Not Be Empty	${response}
	
Add New Transactions Of New Type And Get Sum
	${random_type}	Generate Random String
	${random}	Evaluate    random.sample(range(1, 1000000), 1)    random
	${random}	Get From List	${random}	0
	${status}	${response}	Add New Transaction	${random}	${random_type}	${10}	${1}
	Should Be Equal As Integers	${status}	200
	${random}	Evaluate    random.sample(range(1, 1000000), 1)    random
	${random}	Get From List	${random}	0
	${status}	${response}	Add New Transaction	${random}	${random_type}	${10}	${1}
	Should Be Equal As Integers	${status}	200
	${status}	${response}	Get Transactions By Type	${random_type}
	Should Be Equal As Integers	${status}	200
	Should Not Be Empty	${response}
	${status}	${response}	Get Transaction Sum	1
	Should Be Equal As Integers	${status}	200
	Dictionary Should Contain Key	${response}	sum
	${sum}	Get From Dictionary	${response}	sum
	Should Be True	${sum} > 0