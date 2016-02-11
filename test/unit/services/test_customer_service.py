from nose.tools import assert_equals
from mock import *

from tdd_example.app.services.customer_service import CustomerService


class TestCustomerService():

    def test_should_return_validator_error_message_if_input_is_invalid(self):
        # arrange
        validator = Mock()
        validator_error_response = {'is_valid': False, 'errors': ['Name was invalid']}
        validator.validate_input.return_value = validator_error_response

        service = CustomerService(validator)
        response = service.save_customer('invalid_input')

        assert_equals(validator_error_response, response)

    def test_should_save_customer_information_if_input_is_valid(self):
        # arrange
        validator = Mock()
        repository = Mock()
        valid_response = {'is_valid': True, 'errors': []}
        validator.validate_input.return_value = valid_response

        service = CustomerService(validator, repository)
        service.save_customer('valid_input')

        assert repository.save.called()