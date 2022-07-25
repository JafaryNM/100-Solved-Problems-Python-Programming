"""
📌 Description:
Write a Python program that checks if a list is empty or not.

If the list is empty, print "Empty". Else, print "Not Empty".
📌 Output:
[]--> Return empty
[3,4,7,] --> Return not empty.

If the list is empty, print "Empty". Else, print "Not Empty".


############## Solution 1 ##############

my_list=[3, 5, 8]

if len(my_list)==0:
    print("Empty")
else:
    print("Not Empty")


################# Solution 2 #############

my_list=[3,3,3]

# Not is used to check if elements is empty
if not my_list:
    print("Empty")
else:
    print("Not Empty")

"""
############# Solution 3 ##################

my_list=[]

if my_list:
    print("Not Empty")
else:
    print("Empty")








