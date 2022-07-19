##################### PROBLEM 8 ##########

"""

Write a Python program that prints the string s with the character curr_char replaced by the character new_char.

curr_char and new_char are variables that contain strings with a single character.

You may assume that new_char will not be an empty string.

The match must be case-sensitive (do not replace lowercase letters if curr_char is uppercase).

If no match is found, print the initial string

"""
"""
Output of Code





"""

################# Solution 1 ##############
s= 'Hello'
new_s=""

curr_char= "l"
new_char="d"

for char in s:
    if  char==curr_char:
        new_s=new_char
    else:
        new_s+=char
print(new_s)











