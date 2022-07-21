"""

📌 Description:
Write a Python program to count the number of repeated characters in the string s.

The program must print the total number of repeated characters and a message on the next line displaying the repeated characters separated by a space and sorted alphabetically.

If there are no repeated characters in the string, print 0 as the total count and None on the next line.

🔹 Expected Output:
Output



"""

############ Solution1 ###############

s = "Helloo"

#repeated_count = 0  # By default should start with zero because no repeated characters
repeated_chars = []  # List to store repeated characters

for char in s:
    # if apper more than one   and not in repeated_in lists
    if (s.count(char)>1) and (char not in repeated_chars):
        #repeated_count+=1
        repeated_chars.append(char)
print(len(repeated_chars))
# check if there repeated characters

"""
if len(repeated_chars)>0:
    for char in sorted(repeated_chars): # Should return value in alphabetical order
        print(char, end=" ") # print second value but in same line by adding space

else:
    print(None)
"""

######### Checking if there repeated character ######

if repeated_chars: # Use truthly values
    print(*sorted(repeated_chars),sep=" ") # unpacked trick
else:
   print (None)