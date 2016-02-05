import copy

from nose.tools import assert_false, assert_true, assert_equals
from numpy.testing import assert_array_equal

from tdd_example.app.utils.input_validator import InputValidator


class TestInputValidator():

    def setup(self):
        self.validator = InputValidator()

    def test_should_return_identifier_type_error_message_if_identifier_type_is_invalid(self):
        #arrange
        invalid_input = self.__create_default_input(identifier_type="invalid type")
        # act
        result = self.validator.validate_input(invalid_input)

        #assert
        assert_equals({"is_valid": False, "errors": ["Identifier type is invalid"]}, result)

    def test_should_return_is_valid_if_type_cedula(self):
        #arrange
        valid_input = self.__create_default_input(identifier_type="cedula")
        # act
        result = self.validator.validate_input(valid_input)

        #assert
        assert_equals({"is_valid": True, "errors": []}, result)

    def test_should_return_is_valid_if_type_ruc(self):
        #arrange
        valid_input = self.__create_default_input(identifier_type="ruc")
        # act
        result = self.validator.validate_input(valid_input)

        #assert
        assert_equals({"is_valid": True, "errors": []}, result)

    def test_should_return_identifier_type_error_message_if_cedula_identifier_has_only_9_digits(self):
        #arrange
        invalid_input = self.__create_default_input(identifier="123456789")
        # act
        result = self.validator.validate_input(invalid_input)

        #assert
        assert_equals({"is_valid": False, "errors": ["Identifier is invalid for the given type"]}, result)

    def test_should_return_identifier_type_error_message_if_cedula_identifier_has_a_letter(self):
        #arrange
        invalid_input = self.__create_default_input(identifier="1234E67890")
        # act
        result = self.validator.validate_input(invalid_input)

        #assert
        assert_equals({"is_valid": False, "errors": ["Identifier is invalid for the given type"]}, result)

    def test_should_return_identifier_type_error_message_if_cedula_first_two_digits_are_greater_than_24(self):
        #arrange
        invalid_input = self.__create_default_input(identifier="2534567890")
        # act
        result = self.validator.validate_input(invalid_input)

        #assert
        assert_equals({"is_valid": False, "errors": ["Identifier is invalid for the given type"]}, result)

    def test_should_return_identifier_type_error_message_if_cedula_first_two_digits_are_00(self):
        #arrange
        invalid_input = self.__create_default_input(identifier="0034567890")
        # act
        result = self.validator.validate_input(invalid_input)

        #assert
        assert_equals({"is_valid": False, "errors": ["Identifier is invalid for the given type"]}, result)


    def test_should_return_true_if_cedula_has_only_10_digits(self):
        #arrenge
        valid_input = self.__create_default_input(identifier="1234567890")
        # act
        result = self.validator.validate_input(valid_input)

        # assert
        assert_equals({"is_valid": True, "errors": []}, result)


    def test_should_return_true_if_first_two_digits_are_between_1_to_24(self):

        for first_digits_number in range(1, 25):
            #arrange
            zero = "0" if first_digits_number < 10 else ""
            cedula = "{0}{1}34567890".format(zero, first_digits_number)

            valid_input = self.__create_default_input(identifier=cedula)

            # act
            result = self.validator.validate_input(valid_input)

            # assert
            assert_equals({"is_valid": True, "errors": []}, result)

    def test_should_return_false_if_first_name_is_empty_string(self):
        #arrange
        valid_input = self.__create_default_input(name="")
        #act
        result = self.validator.validate_input(valid_input)

        # assert
        assert_equals({"is_valid": False, "errors": ["Name should not be empty"]}, result)

    def test_should_return_false_if_first_name_is_none(self):
        #arrange
        valid_input =  self.__create_default_input(name=None)
        #act
        result = self.validator.validate_input(valid_input)

        # assert
        assert_equals({"is_valid": False, "errors": ["Name should not be empty"]}, result)


    def test_should_return_true_if_string_is_Karina(self):
        #arrange
        valid_input =  self.__create_default_input(name="Karina Mora")
        #act
        result = self.validator.validate_input(valid_input)

        # assert
        assert_equals({"is_valid": True, "errors": []}, result)

    def test_should_return_error_if_input_is_incomplete(self):
        #arrange
        input = {}

        #act
        result = self.validator.validate_input(input)

        # assert
        assert_equals({"is_valid": False, "errors": ["Input is incomplete"]}, result)

    def test_should_return_amount_deficit_error_if_deposit_is_less_than_200(self):
        #arrange
        invalid_input =  self.__create_default_input(deposit=199)
        #act
        result = self.validator.validate_input(invalid_input)

        # assert
        assert_equals({"is_valid": False, "errors": ["Deposit should be at least $200"]}, result)

    def test_should_return_all_error_there_are_many_invalid_fields(self):

        #arrange
        invalid_input =  self.__create_default_input(deposit=199, name="")
        #act
        result = self.validator.validate_input(invalid_input)

        # assert
        assert_false(result["is_valid"])
        assert_array_equal(sorted(["Deposit should be at least $200", "Name should not be empty"]), sorted(result["errors"]))


    def __create_default_input(self, identifier_type="cedula",
                               identifier="1712345670",
                               name="Someone Valid",
                               deposit=200):
        return {
            "identifier_type": identifier_type,
            "identifier": identifier,
            "name": name,
            "deposit": deposit
        }
