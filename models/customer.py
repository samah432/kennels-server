

class Customer:

    def __init__(self, id, name, status, customer_id):
        self.id = id
        self.name = name
        self.status = status
        self.customer_id = customer_id


# Create a new Customer object.
new_customer = Customer(1, "John", "Admitted", 4)