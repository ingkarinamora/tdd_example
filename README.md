# tdd_example

This workshop will help to practice TDD.

Prerequisites:
- Python (already in the Mac)
- Nose (sudo easy_install nose)
- pip (sudo easy_install nose)
- Flask (sudo pip install flask)

- Install:
  Pycharm (https://www.jetbrains.com/pycharm/download/)
  MongoDb (https://www.mongodb.org/downloads#production)  

First we will create a Monolithic:

1.- One end point should have the following data:
- An identifier type that should be one of the following types:
  Cedula
  Passport
  RUC
- An identifier number that should have a valid structure for each type
- A first name and last name that should not be empty
- The accounts numbers with their initial amount that should be al least of $200
This input should be validated and the customer should be persisted in a MongoDb database,
giving the appropriate response.

2.- Another service should register money deposit for a customer, by using the following data:
- An account number
- An amount of money deposited
This deposit should be persisted and the customer should be persisted,
giving the appropriate response.

3.- Another endpoint should retrieve the customer:
- An identifier type that should be one of the following types:
  Cedula
  Passport
  RUC
- An identifier number that should have a valid structure for each type

4.- Another endpoint should retrieve all the deposits for a given customer by account:
- An identifier type that should be one of the following types:
  Cedula
  Passport
  RUC
- An identifier number that should have a valid structure for each type
