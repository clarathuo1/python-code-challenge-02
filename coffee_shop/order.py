class Order:
    def _init_(self, customer, coffee, price):
# Validate that the price is a float and is between 1.0 and 10.0
        if not isinstance(price, (int,float)) or not(1.0 <= price <= 10.0):
            raise ValueError("Price must be a number between 1.0 and 10.0 ")
#  Validate that customer is a Customer object and coffee is a Coffee object
        if not isinstance(customer, Customer) or not isinstance(coffee, Coffee):
            raise ValueError("Customer and Coffee must be valid objects")

# Assign the customer, coffee, and price to the order instance
        self.customer = customer
        self.coffee = coffee
        self.price = price

# Customer property (read-only)
        @property
        def customer(self):
            return self._customer

# Coffee property (read-only)
        @property
        def coffee(self):
            return self._coffee

# Price property (read-only)
        @property
        def price(self):
            return self._price