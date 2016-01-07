from random import randint

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

    def test_should_return_true_if_type_is_ruc(self):
        # act
        result = self.validator.validate_customer_type('ruc')

        # assert
        assert_true(result)

    def test_should_return_false_if_cedula_has_only_9_digits(self):
        # act
        result = self.validator.validate_cedula('123456789')

        # assert
        assert_false(result)

    def test_should_return_false_if_cedula_has_a_letter(self):
        # act
        result = self.validator.validate_cedula('1234E67890')

        # assert
        assert_false(result)

    def test_should_return_true_if_cedula_has_only_10_digits(self):
        # act
        result = self.validator.validate_cedula('1234567890')

        # assert
        assert_true(result)

    def test_should_return_false_if_first_two_digits_are_greater_than_24(self):
        # act
        result = self.validator.validate_cedula('2534567890')

        # assert
        assert_false(result)

    def test_should_return_false_if_first_two_digits_are_00(self):
        # act
        result = self.validator.validate_cedula('0034567890')

        # assert
        assert_false(result)

    def test_should_return_true_if_first_two_digits_are_between_1_to_24(self):

        for first_digits_number in range(1, 25):
            #arrange
            zero = '0' if first_digits_number < 10 else ''
            cedula = '{0}{1}34567890'.format(zero, first_digits_number)

            # act
            result = self.validator.validate_cedula(cedula)

            # assert
            assert_true(result)

    def test_should_return_false_if_first_name_is_empty_string(self):
        #act
        result = self.validator.validate_non_empty_letters_string('')

        # assert
        assert_false(result)

    def test_should_return_false_if_first_name_is_none(self):
        #act
        result = self.validator.validate_non_empty_letters_string(None)

        # assert
        assert_false(result)

    def test_should_return_true_if_string_is_Karina(self):
        #act
        result = self.validator.validate_non_empty_letters_string('Karina')

        # assert
        assert_true(result)
