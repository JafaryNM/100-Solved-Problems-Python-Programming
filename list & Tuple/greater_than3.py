"""
📌 Description:
Write a Python program that counts the number of elements in a list with value greater than 3.

You may assume that the list only contains numbers.

Print the final count

"""
############### Solutio 1 ##############

my_list=[1,2,3,4,5,5,6,7]
count=0

for element in my_list:
    if element>3:
        count+=1
print(count)

############## Solution 2 ###############
my_list=[6,7,8]

count=sum(1 for element in my_list if element>3)










