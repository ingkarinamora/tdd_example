from abc import ABCMeta, abstractmethod


class ErrorValidate(Exception):

    def __init__(self, value):
         self.value = value

    def __str__(self):
        return repr(self.value)


class IValidate:
    __metaclass__ = ABCMeta

    @abstractmethod
    def validate(self, input): raise NotImplementedError


class ValidateIdentifierType(IValidate):
    def validate(self, input):
        customer_type = input["identifier_type"]
        if not customer_type in ["cedula", "ruc"]:
            raise ErrorValidate(InputValidator._error_messages["identifier_type_error"])
        return True


class ValidateCedula(IValidate):
    def validate(self, input):
        cedula = input["identifier"]
        if not (len(cedula) == 10 and cedula.isdigit() and 0 < int(cedula[:2]) < 25):
            raise ErrorValidate(InputValidator._error_messages["identifier_error"])
        return True


class ValidateNonEmptyLettersString(IValidate):
    def validate(self, input):
        name = input["name"]
        if not name:
            raise ErrorValidate(InputValidator._error_messages["name_error"])
        return True


class ValidateDepositAmount(IValidate):

    def validate(self, input):
        amount = input["deposit"]
        if not amount >= 200:
            raise ErrorValidate(InputValidator._error_messages["deposit_error"])
        return True



class InputValidator():
    _error_messages = {
        "incomplete_input_error": "Input is incomplete",
        "identifier_type_error": "Identifier type is invalid",
        "identifier_error": "Identifier is invalid for the given type",
        "name_error": "Name should not be empty",
        "deposit_error": "Deposit should be at least $200"
    }


    def validate_input(self, input):
        errors = []
        validators = [ValidateIdentifierType(), ValidateCedula(), ValidateNonEmptyLettersString(), ValidateDepositAmount()]
        if all([key not in input for key in ["identifier_type", "identifier", "name"]]):
            return self.__create_validity_response([self._error_messages["incomplete_input_error"]])

        for val in validators:
            try:
                val.validate(input)
            except ErrorValidate as error_validate:
                errors.append(error_validate.value)


        return self.__create_validity_response(errors)


    def __create_validity_response(self, error=None):

        return {
            "is_valid": False if error else True,
            "errors": error
        }


