"""
📌 Description:
Write a Python program that prints a version of the string s with all commas replaced by dots

📌 Output:
"Hello World"--> Print  Hello. World
"3,29292"--> Print 3.29292


########### Solution 1 ##############

s= "Hello , World"
new_s=""
COMMA=","
DOT="."

# Take all value of s put in char
for char in s:
    # check if there  comma in string
    if (char==COMMA):
        new_s+=DOT
    else:
        new_s+=char
print(new_s)

"""
########### Solution 2 #########

s="3,449,494"
COMMA=","
DOT="."
# Replace Comma with Dot
print(s.replace(COMMA,DOT))



