from tdd_example.app.domain.customer import Customer


class CustomerRepository:

    def __init__(self, db):
       self.db = db

    def save(self, customer_data):
        self.db.customer.insert(self.encode_custom(customer_data))

    def get_by_identifier(self, customer_id):
        customer = self.decode_custom(self.db.customer.find_one({"identifier": customer_id}))
        return customer

    def encode_custom(self, customer):
        return {"_type": "customer", "identifier_type": customer.identifier_type(),
                "identifier": customer.identifier(), "name": customer.name()}

    def decode_custom(self, document):
        assert document["_type"] == "customer"
        customer = Customer(document["identifier_type"], document["identifier"], document["name"])
        return customer