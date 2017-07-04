# Python is called an "object-oriented programming language."
# This means there is a construct in Python called a class that lets you structure your software in a particular way

# A "module" is like one of these files that I am saving that I can run by importing

# For instance if I create and save a module called stuff.py

# it contains a function

def apple():
    print("I AM APPLES!")

# and a variable
tangerine = "Living reflection of a dream"


# I import it and access the function and print the variable like so:

import stuff
stuff.apple()
print(stuff.tangerine)

# comparing retrieving from dictionaries vs modules

mystuff['apple'] # get apple from dict, the ket is a string ['key']
mystuff.apple() # get apple from the module, the key is an identifier .key
mystuff.tangerine # same thing, it's just a variable


# This means we have a very common pattern in Python:
#    Take a key=value style container.
#    Get something out of it by the key's name.

# Think of a module as a specialized dictionary that can store Python code
# so you can access it with the . operator

# The class version of the stuff module looks like this:
# a class is like a mini-module, but you can have loads whereas you can only
# import one module

class Stuff(object):

# init is the class version of "import" for a module

    def __init__(self):
        self.tangerine = "And now a thousand years between"

    def apple(self):
        print("I AM CLASSY APPLES!")


# you then 'create' this class by calling it like a function

thing = MyStuff()
thing.apple()
print(thing.tangerine)


# Python looks for MyStuff() and sees that it is a class you've defined.
# Python crafts an empty object with all the functions you've specified in the class using def.
# Python then looks to see if you made a "magic" __init__ function, and if you
# have it calls that function to initialize your newly created empty object.
# In the MyStuff function __init__ I then get this extra variable self, which is
# that empty object Python made for me, and I can set variables on it just like you would with a module, dictionary, or other object.
# In this case, I set self.tangerine to a song lyric and then I've initialized this object.
# Now Python can take this newly minted object and assign it to the thing variable for me to work with.



# Classes are like blueprints or definitions for creating new mini-modules.
# Instantiation is how you make one of these mini-modules and import it at the same time.
# "Instantiate" just means to create an object from the class.
# The resulting created mini-module is called an object, and you then assign it to a variable to work with it.


class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])


choice = input("Please choose a song \n")

if (choice) == "hey":

    happy_bday.sing_me_a_song()
else:
    bulls_on_parade.sing_me_a_song()
