"""
📌 Description:
Write a Python program that checks if the string s starts with the sequence of characters denoted by the variable prefix.

If it does, print True. Else, print False.

This test should be case sensitive. For example, "A" should not be equivalent to "a".

If the length of the prefix is greater than the length of the string, print False.

📌 Output:
"Hello"  Prefix He print True
"Coding" Prefix Con Should Print False
"Amazing" Prefix Ame Should  Print False


############### Solution 1 ##############

s = "Hello"
prefix = "Test"

print(s[:len(prefix)]==prefix)
"""
############## Solution 2 ##############
s="Hello"
prefix="He"

print(s.startswith(prefix))




