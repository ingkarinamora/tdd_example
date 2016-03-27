from nose.tools import assert_equals,assert_not_equals
from tdd_example.app.domain.customer import Customer


class TestCustomer():

    def test_should_create_customer_with_properties(self):

        customer = Customer ('identifier_type', 'identifier', 'name')

        assert_equals('identifier_type', customer.identifier_type())
        assert_equals('identifier', customer.identifier())
        assert_equals('name', customer.name())


    def test_should_return_false_when_compare_two_diferents_customer(self):
        customerOne = Customer ('identifier_type', 'identifier', 'name')
        customerTwo = Customer ('identifier_type', 'other_identifier', 'name')

        assert_not_equals(customerOne, customerTwo)

    def test_should_return_true_when_compare_two_equals_customer(self):
        customerOne = Customer ('identifier_type', 'identifier', 'name')
        customerTwo = Customer ('identifier_type', 'identifier', 'name')

        assert_equals(customerOne, customerTwo)