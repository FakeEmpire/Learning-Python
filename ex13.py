# we are adding features (called modules) to our Python script from the Python feature set

from sys import argv
# read the WYSS section for how to run this
script, first, second, third = argv

# the argument variable argv holds the argument you pass to the script when run
# line 5 unpacks argv and assigns its contents to those variables

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)



#When you are running anything with the argv you must pass command line arguments
# instead of typing python ex13.py to run, you must add three more argument names
# in this case

#You can also do the same thing but request the user inputs a variable
#print("The script is called:", script)
#print("Your first variable is:", input("What is your first variable?"))
#print("Your second variable is:", second)
#print("Your third variable is:", third)

# argv means the user has to give inputs in the command line, whereas
# input means they do so as the script is running
