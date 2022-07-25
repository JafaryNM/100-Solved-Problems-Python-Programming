"""
📌 Description:
Write a Python program that multiplies all the items in a list by the value of the variable factor.

The program must print the list as the output.

The program should also allow multiplying the variable factor by a string in case the list contains strings.

You may assume that the value of factor will be a positive integer

📌 Outuput:
Input [1,2,3] factor 2 --> Output should be  [1,4,6]
input [ ' a' , 'b' , 'c' factor 3 --> Outpush should be [' aaa' , ' bbb', 'ccc']

################ Solutions #####################

my_list = [1, 2,3]
factor = 3

for i in range (len(my_list)):
     my_list[i]*=factor
print(my_list)

"""
######################### Solution 2 #################\


my_list=[2,4,6,8]
factor=3

for i, elem in enumerate(my_list): #   [ (0,2),(1,4),(2,6),(3,8)
                                                     #      i, e   i, e    i ,e   i,e
   my_list[i]=elem*factor

print(my_list)








