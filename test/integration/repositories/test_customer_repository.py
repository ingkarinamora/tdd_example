from nose.tools import assert_equals
from pymongo import MongoClient
from tdd_example.app.domain.customer import Customer
from tdd_example.app.repositories.customer_repository import CustomerRepository


class TestCustomerRepository:
    def setup(self):
        self. mongo_client = MongoClient()
        self.mongo_client.drop_database("db_test")
        self.db = self.mongo_client.test

    def test_should_save_customer(self):

        identifier_type = 'some_type'
        identifier = 'any_identifier'
        name = 'Customer Name'
        customer = Customer(identifier_type, identifier, name)

        repository = CustomerRepository(self.db)
        repository.save(customer)
        customer_save = repository.get_by_identifier('any_identifier')
        assert_equals(customer.identifier_type(),customer_save.identifier_type())

