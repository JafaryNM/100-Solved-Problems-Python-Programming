##################### PROBLEM 4 ##########

"""

Write a Python program that prints the first and last three characters of the string s as a single string.

If the string has less than six characters, print an empty string (blank output).ntact.


OUTPUT 
 "Blue" --> Print out ""
 "Wonderful"  --> Print out "Wonful"
 "Amazing"   --> "Amaing"
 


############# Solutions 1 ###################

s="Amazing"  # len (s)-> 9
               # W o n d e r f u l
               # 0 1 2 3 4 5 6 7 8


# If stirng not contain an less than six charaters should print empty string

if len(s)<6:
    print("")

# The print first three and last three characters
                                                                      
else:
    new_string= s[:3] +s[len(s)-3:] # default value is equivalent to  s[0:3] last value excluded 
                                    # return  Won  return ful  form s[(9-3):] 
    print(new_string)               # finally return  WonFul
"""

################ Solution 2 ####################

s ='Wonderful'

num_char=3

if len(s)< num_char*2:
    print("")

else:
    new_string=s[:num_char] + s[len(s)-num_char:]
    print(new_string)
