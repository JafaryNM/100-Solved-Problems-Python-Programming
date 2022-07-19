"""
📌 Description:
Write a Python program that prints a copy of the string s without any spaces.

Words should be connected in the final string.

If the string doesn't contain spaces, print it intact
📌 Output

Hello print  Hello
Important is very good   print Importantisverygood


############### Solutions 1 ###############

s="Hello Word"
new_s=""

for char in s:
    if char !=" ":
        new_s+=char
print(new_s)

"""
################## Solution 2 ##################

s= "Hello World"

# Using replace method in python programing language
print(s.replace(" ",""))






