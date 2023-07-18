




class Location:

    def __init__(self, id, name, status, customer_id):
        self.id = id
        self.name = name
        self.status = status
        self.customer_id = customer_id


# Create a new Location object.
new_location = Location(1, "Nashville", "Recreation", 1)