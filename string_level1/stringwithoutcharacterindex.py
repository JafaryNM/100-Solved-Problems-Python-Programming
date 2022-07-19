##################### PROBLEM 7 ##########

"""

Write a Python program that prints the string s without the character at index n.

If the index n is out of range, print the string s intact.

If the string s is empty, print the string s intact

"""

############# Solution 1 ##################3
"""
s='Hello'
n=2
# Checking if string is empty or number enter is out of  range
if  (len(s)==0) or (n>=len(s)):
    print(s)

else:
    new_s=""
    for i in range(len(s)):
        if i !=n:
            new_s+=s[i]
    print(new_s)
"""

############### Solution  2 ###############

s= "Hello"
n=2

# Checking string is empty or n is greater than string
# not is good to check if string is empty is return true

if (not s) or (n>len(s)):
    print(s)
else:
    new_s=""
    for i in range(len(s)):
        if i!=n:
            new_s+=s[i]
    print(new_s)


























