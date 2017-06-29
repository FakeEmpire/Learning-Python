#Functions do three things:

    # They name pieces of code the way variables name strings and numbers.
    # They take arguments the way your scripts take argv.
    # Using 1 and 2, they let you make your own "mini-scripts" or "tiny commands."

#use def to define a Function and then give the function name

def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

# this just takes one argument
def print_one(arg1):
    print(f"arg1: {arg1}")

# this one takes no arguments
def print_none():
    print("I got nothin'.")


print_two_again("Amber","Gibney")
print_one("First!")
print_none()


# many ways of assigning values to function for printing

#1. first we define the function

def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")

#1a. we can give the numbers directly
print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)

# we can also ask for an input
print("We can just give the function numbers directly:")
cheese_and_crackers(int(input("Please enter number of cheeses you have")), 30)


#1b. we can define variables and pass them values
print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

#1c. We can do maths to get the values
print("We can even do maths inside too:")
cheese_and_crackers(10 + 20, 5 + 6)


print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
