"""
📌 Description:
Write a Python program that removes duplicate elements from a list, only keeping one occurrence of each element in the list.

The original list should be mutated (modified).

The program must print the final version of the list.
"""

######## Solution 1 ##############

my_list=[1,2,3,4,4]
no_duplicate=list(set(my_list)) # Set data structure remove duplicate
print(no_duplicate)


############# Solution 2 ###########

my_list=[2,2, 3, 4,5,5]
no_dupicate_list=list(dict.fromkeys(my_list))
print(no_dupicate_list)

# dict.fromkeys(my_list)
# {2:None, 3:None , 4:None 5:None,}--> Return list from dictionary














