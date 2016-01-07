class InputValidator():
    def validate_customer_type(self, customer_type):
        return customer_type in ['cedula', 'ruc']

    def validate_cedula(self, cedula):
        return len(cedula) == 10 and cedula.isdigit() and 0 < int(cedula[:2]) < 25

    def validate_non_empty_letters_string(self, first_name):
        if first_name:
            return True
        return False
