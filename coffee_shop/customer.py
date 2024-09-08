
class Customer:
    def __init__(self, name):
        #Initialize a Customer instance with a name.
        if not isinstance(name, str) or not 1 <= len(name) <= 15:
            raise ValueError("Name must be a string between 1 and 15 characters")
        self._name = name

    @property
    def name(self):
        #Return the customer's name.
        return self._name

    @name.setter
    def name(self, value):
        #Set the customer's name.
        
        if not isinstance(value, str) or not 1 <= len(value) <= 15:
            raise ValueError("Name must be a string between 1 and 15 characters")
        self._name = value