# Most of the uses of inheritance can be simplified or replaced with composition
# and multiple inheritance should be avoided at all costs.

# here we create a parent class and a child class that inherits from it



class Parent(object):

    def override(self):
        print("PARENT override()")

    def implicit(self):
        print("PARENT implicit()")

    def altered(self):
        print("PARENT altered()")

class Child(Parent):


# note here that override is going to override the inheritance from the Parent
# class
    def override(self):
        print("CHILD override()")

# in this case, super (Child, self) looks for the parent class of Child
# and then returns Parent.altered()
    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        super(Child, self).altered()
        print("CHILD, AFTER PARENT altered()")

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()



# Using composition instead of inheritance
# good for has-a rather than is-a relationships

class Other(object):

    def override(self):
        print("OTHER override()")

    def implicit(self):
        print("OTHER implicit()")

    def altered(self):
        print("OTHER altered()")

class Child(object):

    def __init__(self):
        self.other = Other()

    def implicit(self):
        self.other.implicit()

    def override(self):
        print("CHILD override()")

    def altered(self):
        print("CHILD, BEFORE OTHER altered()")
        self.other.altered()
        print("CHILD, AFTER OTHER altered()")

son = Child()

son.implicit()
son.override()
son.altered()

# In this case the child class takes what it needs from other, not everthing
