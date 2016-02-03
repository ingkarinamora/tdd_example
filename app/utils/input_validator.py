class InputValidator():

    def validate_input(self, input):
        errors = []

        if all([key not in input for key in ['identifier_type', 'identifier', 'name']]):
            return self.__create_validity_response(["Input is incomplete"])

        if not self.__validate_identifier_type(input.get("identifier_type")):
            errors.append("Identifier type is invalid")

        if not self.__validate_cedula(input.get("identifier")):
            errors.append("Identifier is invalid for the given type")

        if not self.__validate_non_empty_letters_string(input.get("name")):
            errors.append("Name should not be empty")

        return self.__create_validity_response(errors)

    def __validate_identifier_type(self, customer_type):
        return customer_type in ["cedula", "ruc"]

    def __validate_cedula(self, cedula):
        return len(cedula) == 10 and cedula.isdigit() and 0 < int(cedula[:2]) < 25

    def __validate_non_empty_letters_string(self, first_name):
        if first_name:
            return True
        return False

    def __create_validity_response(self, error=None):

        return {
            "is_valid": False if error else True,
            "errors": error
        }

