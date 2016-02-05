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

        if all([key not in input for key in ["identifier_type", "identifier", "name"]]):
            return self.__create_validity_response([self._error_messages["incomplete_input_error"]])

        if not self.__validate_identifier_type(input.get("identifier_type")):
            errors.append(self._error_messages["identifier_type_error"])

        if not self.__validate_cedula(input.get("identifier")):
            errors.append(self._error_messages["identifier_error"])

        if not self.__validate_non_empty_letters_string(input.get("name")):
            errors.append(self._error_messages["name_error"])

        if not self.__validate_deposit_amount(input.get("deposit")):
            errors.append(self._error_messages["deposit_error"])

        return self.__create_validity_response(errors)

    def __validate_identifier_type(self, customer_type):
        return customer_type in ["cedula", "ruc"]

    def __validate_cedula(self, cedula):
        return len(cedula) == 10 and cedula.isdigit() and 0 < int(cedula[:2]) < 25

    def __validate_non_empty_letters_string(self, first_name):
        if first_name:
            return True
        return False

    def __validate_deposit_amount(self, amount):
        return amount >= 200

    def __create_validity_response(self, error=None):

        return {
            "is_valid": False if error else True,
            "errors": error
        }

