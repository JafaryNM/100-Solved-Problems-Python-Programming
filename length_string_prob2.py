##################### PROBLEM 2 ##########

"""

Write a Python program that prints the character at index i in the string s.

If the index is out of range, the program should print "i is out of range"

If the string is empty, the program should print "Empty String
    

"""
"""
OUTPUT 


 Hello   if i=2 print  l
 Pizza  if  i=4 print  a
 ""      print empty string
 "hello" if  i=15   i   print out of range
 
 

"""

############# SOLUTIONS ################


######## OPTION 1  ########

s= "hello"   # h e l l o

i=3         # 0 1 2 3 4

# Check firs if string is empty

if (len(s)==0):
    
    print ("String is empty")

# Check not allowed to print list outside the list

elif(i<len(s)):
    
    print(s[i])

else:
    
    print("i ia out of range")















