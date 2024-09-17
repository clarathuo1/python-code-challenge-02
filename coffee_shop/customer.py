class Customer:
    def _init_(self, name):
        self.name = name
        self._validate_name()
                
# getter for name property
    @property
    def name(self):
        return self._name

# setter for name property
    @name.setter
    def name(self, new_name):
    # validate
        if not isinstance(self._name, str) or not(1 <= len(self._name) <= 15):
            raise ValueError("Name must be a string and between 1 and 15 characters long")
        self._name = new_name

# class-level attribute
    _orders = []

# Return a list of all orders associated with this customer
    def orders(self):
        return [order for order in Customer._orders if order.customer == self]

# Return a unique list of all coffees the customer has ordered
        def coffee(self):
            return list({order.coffee for order in self.orders()})

#  Create a new order for this customer
        def create_order(self, coffee, price):
# Create a new order instance
            new_order = Order(self, coffee, price)
# Add the order to the class-level _orders list
            Customer._orders.append(order)
            return order


# Class method to find the customer who has spent the most on a specific coffee
    @classmethod
    def most_aficionado(cls, coffee):
# Filter orders by the coffee provided
        coffee_orders = [order for order in cls._orders if order.coffee == coffee]
        if not coffee_orders:
            return None
#  Find the customer who has spent the most on this coffee
        return max(coffee_orders, key=lambda order: order.price).customer