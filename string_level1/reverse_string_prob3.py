##################### PROBLEM 3 ##########

"""

Write a Python Program that prints the reversed version of a string.

The program must preserve uppercase and lowercase letters.

If the string is empty, print it intact.

"""
"""

OUTPUT 
 "Hello" --> Print out  "olleh"
 "Woo"  --> Print out "oow"
 ""   --> ""
"""

######## OPTION ONE SOLUTIONS ####################

from audioop import reverse


s= "hello"

#  Solving using String slicing 
print(s[::-1])  # strings = start:stop:step indications
                # string =            :: step means returns data in reverse directions



################# OPTION TWO SOLUTIONS ##################

string="Amazing solution"

# Assign reverse values in certain variable

reverse_string= string[::-1]
print(reverse_string)

################# OPTION THREE SOLUTIONS ##################

# Reverse string will join built function

stringr_join="Delicious"

# return reversed("hello")--> return ["o","l","l","e","h"]
# join built fn come to action "".join(["o","l","l","e","h"])--> return "olleh"

reverse_stringr_join="".join(reversed(stringr_join))

print(reverse_stringr_join)

