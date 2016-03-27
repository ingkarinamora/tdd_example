from tdd_example.app.repositories.customer_repository import CustomerRepository
from pymongo import MongoClient

class CustomerService:
    def __init__(self, input_validator, repository):
        self.input_validator = input_validator
        self.repository = repository


    def save_customer(self, input):
        input_validity = self.input_validator.validate_input()
        if input_validity['is_valid']:
            self.repository.save()
            pass
        else:
            return input_validity

