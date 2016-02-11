class TestCustomerRepository:

    def test_should_save_customer(self):

        customer_data = {
            "identifier_type": 'some_type',
            "identifier": 'any_identifier',
            "name": 'Customer Name',
        }
        repository = CustomerRepository()
        repository.save(customer_data)

        assert_equals(repository.get('any_identifier'))
