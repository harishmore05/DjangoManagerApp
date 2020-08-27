# Django Manager Project

This project builds API for user and employees. This API are Rest API and designed with the help of Django Resr Framework.

## User API

To access user api: base url is localhost:8000/api/user/*

User this api anyone can do login, logout, create new user.

Don't forget to use */* after every url. For ex: **localhost:8000/api/user/login** won't work use -> **localhost:8000/api/user/login/**

To use this user api here is help section:

1. localhost:8000/api/user/login/ -> send post request with valid email and password
2. localhost:8000/api/user/logout/ -> send get request
3. localhost:8000/api/user/ -> send post request and send user data as payload to create new user

## Employee API

With this employee api, one can create new employee, delete and update employee record.

I have used Serializers and Viewsets to handle api request. 

Serializers are responsible for converting python complex data structure into JSON format. Django Serializers also support Deserialization (Convert JSON data into Python Complex Data type like Django's models)

ViewSets handles the normal get, post API routes by its own.

To use employee API here is help section:

1. localhost:8000/api/employee/ -> If get request, response will be all employee records in JSON format
2. localhost:8000/api/employee/ -> If request = POST and valid employee data, response will be employee record created. (create employee record)
3. localhost:8000/api/employee/ -> If request = DELETE and employee id, response will record deleted. (To delete employee record)
4. localhost:8000/api/employee/ -> If request = PATCH and valid employee data, response will be updated employee data. (To update employee)

## Payment API

I have used braintree gateway to process payment. Its aslo involves the braintree API calls.

Only need to create views in this app as this only involves token based api calls to braintree as wwell as UI side.

Braintree works with following steps of payment:

1. Client will send request to generate token for transaction, at server side django will generate token for transation using braintrees gateway interface (gateway.client_token.generate()) In our case to generate this token url is: **localhost:8000/payment/gettoken/<user_id>/<session_token>/**
2. Server will genrate token and will send this token to UI side for further processing. In our case **localhost:8000/payment/gettoken/<user_id>/<session_token>/** response of this request will token from braintree gateway.
3. Client will genrate nounce and will send it to server. In our case **localhost:8000/payment/gettoken/process/<str:id>/<str:token>/** will get called with valid token and id.
4. Django server will request braintree for payment processing with braintree token and client nounce.
5. Braintree server will response with JSON data about payment like transaction id and transaction amount.