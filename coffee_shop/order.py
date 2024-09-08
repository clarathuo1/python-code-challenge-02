
class Order:
    def __init__(self, customer, coffee, price):
        #Initialize an Order instance with a customer, coffee, and price.
        if not isinstance(customer, Customer) or not isinstance(coffee, Coffee):
            raise ValueError("Customer and coffee must be instances of Customer and Coffee respectively")
        if not isinstance(price, float) or not 1.0 <= price <= 10.0:
            raise ValueError("Price must be a float between 1.0 and 10.0")
        self._customer = customer
        self._coffee = coffee
        self._price = price

    @property
    def customer(self):
        #Return the customer object for that order.
        return self._customer

    @property
    def coffee(self):
        #Return the coffee object for that order.
        return self._coffee

    @property
    def price(self):
        #Return the price for the order.
        return self._price