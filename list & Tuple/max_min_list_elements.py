"""
Write a Python program that prints the largest and smallest values in a list

Print the two values on the same line, separated by a space.

The largest value should appear first and the smallest value should appear second.

You may assume that the list only contains numeric values.

If the list is empty, print None

Output Should be
 Input [3,5,8,0] return max_number =8 and min number= 0

"""
################## Solution 1 #############

my_list= [3, 5,8,0]

if my_list:
     print(max(my_list), min(my_list))
else:
    print(None)







