# reading the contents of text files
# to run type the usual python filename.py filename.txt

from sys import argv

script, filename = argv

txt = open(filename)

print(f"Here's your file {filename}:")
print(txt.read())

# this second bit prompts you to enter the name of the file
print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())


#File commands

# close --    Closes the file. Like File->Save.. in your editor.
# read --     Reads the contents of the file. You can assign the result to a variable.
# readline -- Reads just one line of a text file.
# truncate -- Empties the file. Watch out if you care about the file.
# write('stuff') -- Writes "stuff" to the file.
# seek(0) -- Move the read/write location to the beginning of the file.
