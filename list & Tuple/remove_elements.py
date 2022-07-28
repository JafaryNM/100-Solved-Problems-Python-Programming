""""
📌 Description:
Write a Python program that removes all occurrences of the element elem_to_remove from a list.

The output of the program should be the new list with the element removed.

If the element is not found in the list, print the message "Not Found".

If the list is empty, print "Empty List".
"""

############# Solution 1 ###################


my_list =  [1, 2, 3, 4]
remove_element=3

# Checking list  is empty

if not my_list:
 print ("Empty list")

# Checkint number inside list

elif my_list.count(remove_element)==0:
 print("Not found")

else:
 for i in range(my_list.count(remove_element)):
  my_list.remove(remove_element)

print(my_list)






