# Web Service Architecture
Python + Flask is been use to create the REST prototype and SQLite3 is been used to store the transaction.

Client -->  REST API ---> SQLITE3

The REST API has a very basic authentication useful to cover and test authentication scenarios. In addition, it has the support for SSL communication (Right now disabled)

We are storing all the information into a single table. The information could have been split into two tables: One for types and other for transactions, but since we don't have any extra requirements, it's better to use a single table to avoid inner joins and improve performances. 
| transaction_id INTEGER PRIMARY KEY | parent_id INTEGER | type VAR-CHAR(255)  | amount DOUBLE|

To connect to the data base we are using a singleton class because connecting to an external DB cost time, and it's better to maintain the connection open.

**Web service location**
 - The Rest Web service is located at *web_service* folder

**Installation**
 - Install python 2.7
 - Install pip or make it available in your PATH
 - pip install -r requirements.txt
 - Run the server
	 5. python server.py

**Server arguments**
 - Host: Used to specify host, defauls to 127.0.0.1
 - Port: In which port to run the API
 - d: If provided run server in debug mode

# Testing Framework
For the framework the techonologoes used are Python + RobotFramework and Locust.

RobotFramework: Key driven framework for acceptance testing, html reports enabled by default and easier to start automation for begginer coders. Sample of report at: https://github.com/Zerl1990/n26/blob/master/api_testing_framework/results/report.html

Locust: Framework for performance testing, everything is defined using code and has better memory usage thatn JMeter

**Why on python and why RobotFramework and Locust?**
Simple, created a common library which contains the abstraction to do the calls to web service (Like a page object for UI automation). The idea is to have a core library which knows the internal details about how to control the web service and re-use that library in both robot and locust. In that way the maintainance is easier, and we can scale the testing without problem.

**Project File Structure**
- library: Core library to control web service and a file with custom robot keys
- resources: Contains a resouce called envs_var which can be used to setup the environment to test in case we have a different endpoint and user
- results: All html results are here
- test_locust: Locust test files, classes to simulate user behavior
- test_robot: Robot files with test cases, right know only to smoke (Should be used for CI) and regression (Negative/Positive TCs)

**How to Install it**
Use pip to install the requeriments defined on requirements.txt
pip install -r requirements.txt

**How to run robot test cases**
- Go to project directory
- robot -d results .\tests_robot\regression.robot
- robot -d results .\tests_robot\smoke.robot

**How to run locust**
- Go to project directory
- locust -f .\tests_locust\api_user_locust.py
