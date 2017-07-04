
# object orientated analysis and design

# The process is as follows:

#    Write or draw about the problem.
#    Extract key concepts from 1 and research them.
#    Create a class hierarchy and object map for the concepts.
#    Code the classes and a test to run them.
#    Repeat and refine.


# example with banking

class Customer(object):
    """A customer of ABC Bank with a checking account. Customers have the
    following properties:

# this creates the blueprint that is used to create customer objects

    Attributes:
        name: A string representing the customer's name.
        balance: A float tracking the current balance of the customer's account.
    """

# self.name and self.balance initialise the object

# its like saying amber.name = Amber Gibney
# or amber.balance = 1000.0

# The rule of thumb is, don't introduce a new attribute outside of the
#  __init__ method, otherwise you've given the caller an object that isn't fully initialized.
# for instance if balance was done separatly, you could have someone call the withdraw
# function before the balance was even assigned

    def __init__(self, name, balance=0.0):
        """Return a Customer object whose name is *name* and starting
        balance is *balance*."""
        self.name = name
        self.balance = balance


# to create a customer object, we call the class as if it is a function
# amber = Customer('Amber Gibney', 1000.0), where amber is the object or instance
# the self parameter refers to the instance, say the name amber in this case
# below, self is the instance of customer that withdraw is being called on

    def withdraw(self, amount):
        """Return the balance remaining after withdrawing *amount*
        dollars."""
        if amount > self.balance:
            raise RuntimeError('Amount greater than available balance.')
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        """Return the balance remaining after depositing *amount*
        dollars."""
        self.balance += amount
        return self.balance

# a function defined in a class (like withdraw and deposit above) is called a
# method and has access to all data in the instance of the class, they can
# access and modify anything set on self, and require an instance of the class
# to be used


# Abstract classes

# If you have cars, vans and motorbikes in your car lot, it would make sense
# to make an overall vehicle class, that these classes inherit attributes from
# so that your code does not have a lot of repetition

# now this looks a bit complicated at the start because we need to create
# a metaclass so that instances cannot be created directly in the vehicle class

from abc import ABCMeta, abstractmethod
class Vehicle(object):
    """A vehicle for sale by Amberco Car Dealership.


    Attributes:
        wheels: An integer representing the number of wheels the vehicle has.
        miles: The integral number of miles driven on the vehicle.
        make: The make of the vehicle as a string.
        model: The model of the vehicle as a string.
        year: The integral year the vehicle was built.
        sold_on: The date the vehicle was sold.
    """

    __metaclass__ = ABCMeta

    base_sale_price = 0
    wheels = 0

    def __init__(self, miles, make, model, year, sold_on):
        self.miles = miles
        self.make = make
        self.model = model
        self.year = year
        self.sold_on = sold_on

    def sale_price(self):
        """Return the sale price for this vehicle as a float amount."""
        if self.sold_on is not None:
            return 0.0  # Already sold
        return 5000.0 * self.wheels

    def purchase_price(self):
        """Return the price for which we would pay to purchase the vehicle."""
        if self.sold_on is None:
            return 0.0  # Not yet sold
        return self.base_sale_price - (.10 * self.miles)

    @abstractmethod
    def vehicle_type(self):
        """"Return a string representing the type of vehicle this is."""
        pass

# then we can have the car and truck classes - note how they inherit from
# vehicle with Vehicle in brackets instead of object

class Car(Vehicle):
    """A car for sale by Amberco Car Dealership."""

    base_sale_price = 8000
    wheels = 4

    def vehicle_type(self):
        """"Return a string representing the type of vehicle this is."""
        return 'car'

class Truck(Vehicle):
    """A truck for sale by Amberco Car Dealership."""

    base_sale_price = 10000
    wheels = 4

    def vehicle_type(self):
        """"Return a string representing the type of vehicle this is."""
        return 'truck'

class Motorcycle(Vehicle):
    """A motorcycle for sale by Amberco Car Dealership."""

    base_sale_price = 4000
    wheels = 2

    def vehicle_type(self):
        """"Return a string representing the type of vehicle this is."""
        return 'motorcycle'
