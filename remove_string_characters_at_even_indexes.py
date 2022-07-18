##################### PROBLEM 5 ##########

"""

Write a Python program that prints the string s without the characters located at even indices.

If the string is empty or only has one character, print it intact.


OUTPUT 
 "Coding" --> Print out "oig"
 "Pizza"  --> Print out "iz"
 "Python"   -->Print  "yin"
 "A" --> Print "A"
 "" -->  Print ""
 

########### Solition 1 #####################


s="Coding"     # C o d i n g  len(s)-->6
               # 0 1 2 3 4 5
               # 0 ............. len(s-1)
new_s=""

for i in range(len(s)):
    # Take only not even number
    
    if i%2!=0:
     new_s+= s[i]
print(new_s)

    range(len(s))--> return start from 0

"""

############ Solution 2 ###################

s= "Coding"
new_s=""

for i in range(1,len(s), 2):
    new_s+= s[1]

print(new_s)

