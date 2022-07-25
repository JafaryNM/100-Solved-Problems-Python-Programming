"""
📌 Description:
Write a Python program that prints the elements of a list on the same line.

The elements should be separated only by a space (not by a comma).

The output should not include the opening and closing square brackets [ ].\

📌 Output:
Input [3,4, 5] ---> Output 3,4, 5
input ["a","b", "c"] -->Output a,b,c



############# Solution 1 ##############

my_list=[2, 3, 4]

for elem in my_list:
    print(elem, end=" ")

"""
########### Solution 2 ############

my_list= [3, 4, 5, 8]

print(*my_list, sep=" ") ###### This is used for unpacking the list






