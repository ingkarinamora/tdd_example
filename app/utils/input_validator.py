class InputValidator():
    def validate_customer_type(self, customer_type):
        if customer_type in ['cedula', 'ruc']:
            return True
        return False