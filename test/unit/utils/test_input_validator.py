from nose.tools import assert_false, assert_true

from tdd_example.app.utils.input_validator import InputValidator


class TestInputValidator():

    def setup(self):
        self.validator = InputValidator()

    def test_should_return_false_if_type_is_invalid(self):
        # act
        result = self.validator.validate_customer_type('invalid type')

        # assert
        assert_false(result)

    def test_should_return_true_if_type_is_cedula(self):
        # act
        result = self.validator.validate_customer_type('cedula')

        # assert
        assert_true(result)

    def test_should_return_true_if_type_is_ruc(self):
        # act
        result = self.validator.validate_customer_type('ruc')

        # assert
        assert_true(result)
