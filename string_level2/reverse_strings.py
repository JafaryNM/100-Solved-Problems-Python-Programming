"""

📌 Description:
Write a Python program that reverses the individual words in the string s and changes their capitalization. Uppercase letters should be printed in lowercase and vice versa.

Assume that the string only contains letters and spaces are used to separate words.

🔹 Expected Output:
 Python is awesome  should print emosewa si nohtyp
 Hello World should print dlroW olleH
"""
#################### Solution  1 ###############


s = "Hello  World"
words_list = s.split(" ") # [ "Hello" , "World"
new_s = " "

for word in words_list:
    reversed_word=word[::-1]  # Appling Reverse
    swapped_case=reversed_word.swapcase() # Convert uppercase to lower case
    new_s+=swapped_case + " " # Return space as origin
new_s.rstrip()
print(new_s)








