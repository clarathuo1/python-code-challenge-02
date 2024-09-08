# Coffee Shop Application
## Overview
This project implements a simple coffee shop domain model using Object-Oriented Programming in Python. It consists of three primary classes: Coffee, Customer, and Order, demonstrating many-to-many relationships and encapsulating core functionality.

## Project Structure 
- venv/bin/include/lib/lib64
- pipfile
- pipfile.lock
- coffee_shop/coffee.py/customer.py/order.py
- README.md


## Setup and Installation
Follow these steps to set up and run the project:

- Clone the Repository
Clone this repository to your local machine:
- git clone https://github.com/clarathuo1/phase3-code-challenge-02
- cd coffee_shop
- Create and Activate Virtual Environment
- Create a virtual environment:
python -m venv venv
- Activate the virtual environment:
pipenv install
- Install the required Python packages

## File Descriptions
- coffee.py: Contains the Coffee class with methods to manage coffee objects, including tracking orders and calculating average prices.

- customer.py: Contains the Customer class with methods to manage customer objects, including creating orders and listing coffees.

- order.py: Contains the Order class that ties together a customer, coffee, and price, and ensures proper validation of these attributes.

## Class Specifications
### Customer Class
#### Attributes:

- name: A string (1-15 characters) representing the customer's name.
- Methods:

- __init__(self, name): Initializes the customer with a name.
- orders(self): Returns a list of orders placed by the customer.
- coffees(self): Returns a unique list of coffees ordered by the customer.
- create_order(self, coffee, price): Creates and returns a new order for the customer.
### Coffee Class
#### Attributes:

- name: A string (minimum 3 characters) representing the coffee's name.
- Methods:

- __init__(self, name): Initializes the coffee with a name.
- orders(self): Returns a list of all orders for the coffee.
- customers(self): Returns a unique list of customers who have ordered the coffee.
- num_orders(self): Returns the total number of times the coffee has been ordered.
- average_price(self): Returns the average price for the coffee based on its orders.
### Order Class
#### Attributes:

- customer: A Customer instance.
- coffee: A Coffee instance.
- price: A float (1.0 - 10.0) representing the order price.
- Methods:

- __init__(self, customer, coffee, price): Initializes the order with a customer, coffee, and price.
- customer(self): Returns the customer object for the order.
- coffee(self): Returns the coffee object for the order.
## Testing
Make sure to run tests frequently to ensure that your code is functioning as expected:

bash
Copy code
pytest
## Contribution
If you wish to contribute to this project, please fork the repository and submit a pull request with your changes. Make sure to include appropriate tests and adhere to the coding standards outlined.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contact
For any questions or issues, please contact Clara Thuo.