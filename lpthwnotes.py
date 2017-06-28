#to run a python file in the powershell, type python file.py.
#remember that you will not be in Python when it finishes, you will be in the command shell
# double quotes mean it's a string

print("I will now count my chickens:")

print("Hens", 25 + 30 / 6.0)
print("Roosters", 100 - 25 * 3 % 4)

print("Now I will count the eggs:")

print(3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6)

print("Is it true that 3 + 2 < 5 - 7?")

print(3 + 2 < 5 - 7)

print("What is 3 + 2?", 3 + 2)
print("What is 5 - 7?", 5 - 7)

print("Oh, that's why it's False.")

print("How about some more.")

print("Is it greater?", 5 > -2)
print("Is it greater or equal?", 5 >= -2)
print("Is it less or equal?", 5 <= -2)


#Variables in strings
#You can embed variables in strings with {}
my_name = 'Zed A. Shaw'
my_age = 35.6 # not a lie
my_height = 74.8 # inches
my_weight = 180 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print(f"Let's talk about {my_name}.")
print(f"He's {my_height} inches tall.")
print(f"He's {my_weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are usually {my_teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right note the use of round()
#to round the total
total = my_age + my_height + my_weight
print(f"If I add {my_age}, {my_height}, and {my_weight} I get {round(total)}.")


#more strings and variables
types_of_people = 10
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'")

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)

#more printing

print("Mary had a little lamb.")
print("Its fleece was white as {}.".format('snow'))
print("And everywhere that Mary went.")
print("." * 10)  # what'd that do?

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch that comma at the end.  try removing it to see what happens
print(end1 + end2 + end3 + end4 + end5 + end6, end=' ')
print(end7 + end8 + end9 + end10 + end11 + end12)


#printing and formatting
formatter = "{} {} {} {}"

# we are using a function to turn the formatter variable into other strings
#we are calling the format function and passing 4 arguments to it
#note that you don't put "" around True and False to turn them into strings
#because Python recognises them as keywords representing concepts

print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))


# still more printing
days = "Mon Tue Wed Thu Fri Sat Sun"

# \n means new line and , leaves a space I think

months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print("Here are the days: ", days)
print("Here are the months: ", months)

#triple quotes means you can put as much as you like on different lines
print("""
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
""")

#tricks for when you need quotation marks to feature in a string

"I am 6'2\" tall."  # escape double-quote inside string
'I am 6\'2" tall.'  # escape single-quote inside string

# \t does a tab
# \\ does a single backslash

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

#Full list of Python escape sequence

#   Escape 	    What it does.
#   \\ 	        Backslash (\)
#   \' 	      Single-quote (')
#   \" 	      Double-quote (")
#   \a 	      ASCII bell (BEL)
#   \b 	      ASCII backspace (BS)
#   \f 	      ASCII formfeed (FF)
#   \n 	      ASCII linefeed (LF)
#   \N{name}  Character named name in the Unicode database (Unicode only)
#   \r 	      Carriage Return (CR)
#   \t 	      Horizontal Tab (TAB)
#   \uxxxx 	  Character with 16-bit hex value xxxx
#   \Uxxxxxxxx 	Character with 32-bit hex value xxxxxxxx
#   \v 	      ASCII vertical tab (VT)
#   \ooo 	    Character with octal value ooo
#   \xhh 	    Character with hex value hh


#Asking questions
#end=' ' tells print to not end the line with a newline character and go to the next line

print("How old are you?", end=' ')
age = input()
print("How tall are you?", end=' ')
height = input()
print("How much do you weigh?", end=' ')
weight = input()

#It asks you to input the answer to the question and then saves it as the variable
#age = int(input()) would store the age as an integer

print(f"So, you're {age} old, {height} tall and {weight} heavy.")


# Asking questions using input as the prompts

age = input("How old are you? ")
height = input("How tall are you? ")
weight = input("How much do you weigh? ")

print(f"So, you're {age} old, {height} tall and {weight} heavy.")
