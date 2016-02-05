class CustomerService:
    def __init__(self, input_validator):
        self.input_validator = input_validator

    def save_customer(self, input):
        input_validity = self.input_validator.validate_input()

        return input_validity

