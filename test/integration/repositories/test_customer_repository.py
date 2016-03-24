from nose.tools import assert_equals
from pymongo import MongoClient

from tdd_example.app.domain.customer import Customer
from tdd_example.app.repositories.customer_repository import CustomerRepository


class TestCustomerRepository:

    def test_should_save_customer(self):
        mongo_client = MongoClient()

        identifier_type = 'some_type'
        identifier = 'any_identifier'
        name = 'Customer Name'
        customer = Customer(identifier_type, identifier, name)

        repository = CustomerRepository(mongo_client)
        repository.save(customer)

        assert_equals(customer, repository.getById('any_identifier'))