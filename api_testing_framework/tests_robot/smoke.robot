*** Settings ***
Variables	../resources/env_vars.py
Library	library.n26_api_keywords.N26Library	${HOST}	${USER}	${PASS}
Library	Collections

*** Test cases ***
Get Existing Transaction
	${status}	${response}	Get Transaction By Id	1
	Should Be Equal As Integers	${status}	200
	Dictionary Should Contain Key	${response}	parent_id
	Dictionary Should Contain Key	${response}	amount
	Dictionary Should Contain Key	${response}	type
	
Get Transactions By Type
	${status}	${response}	Get Transactions By Type	TEST
	Should Be Equal As Integers	${status}	200
	Should Not Be Empty	${response}
	
Get Transaction Sum
	${status}	${response}	Get Transaction Sum	1
	Should Be Equal As Integers	${status}	200
	Dictionary Should Contain Key	${response}	sum
	${sum}	Get From Dictionary	${response}	sum
	Should Be True	${sum} > 0