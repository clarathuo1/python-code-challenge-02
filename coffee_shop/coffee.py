class Coffee:

    def _init_(self, name):
        # Validate that the name is a string and has at least 3 characters
        if not isinstance(name, str) or len(name)<3:
            raise ValueError("Name must be a string and at least 3 characters long")
        # Assign the name to the coffee instance
        self.name = name

  # Name property (read-only)
    @property
    def name(self):
        return self._name

    _orders = []

# Return all orders for this specific coffee
    def orders(self):
        return [order for order in Coffee._orders if order.coffee == self]A

#  Return a unique list of all customers who have ordered this coffee 
    def customer(self):
        return  list({order.customer for order in self.orders()})
    
# Return the total number of orders for this coffee
    def total_orders(self):
        return len(self.orders())

# Return the average price for this coffee based on all orders
    def average_price(self):
        total_price = sum(order.price for order in self.orders())
        num_orders = len(self.orders())
        return total_price / num_orders if num_orders > 0 else 0