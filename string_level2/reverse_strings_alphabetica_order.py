"""
📌 Description:
Write a Python program that reverses the individual words in the string s and changes their capitalization. Uppercase letters should be printed in lowercase and vice versa.

Assume that the string only contains letters and spaces are used to separate words.

📌 Output:





############# Solution 1 #########################

s = " Hello World "
new_s=""
word_list = s.split( " ") # [ "Hello", "Word" ]

for word in word_list:
    lowercase_word=word.lower()
    sorterd_word = " ".join(sorted(lowercase_word))
    new_s+=  sorterd_word + " "
new_s.rstrip()
print(new_s)
"""
############## Solution 2 ###############################

s = "Hello Word"
new_s = " "
world_list = s.split(" ")

for word in world_list:
    new_s = " ".join(sorted(word.lower())) + " "

new_s.rstrip()
print(new_s)