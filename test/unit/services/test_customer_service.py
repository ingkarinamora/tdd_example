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