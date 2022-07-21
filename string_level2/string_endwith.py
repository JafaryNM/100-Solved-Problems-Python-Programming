"""
📌 Description:
Write a Python program that checks if the string s ends with a specific sequence of characters denoted by the variable suffix.

If it does, print True. Else, print False.

This test should be case sensitive. Therefore, "A" should not be equivalent to "a".

If the length of the suffix is greater than the length of the string, print Fals

📌 Output:
"Hello"  Prefix lo print True
"Coding" Prefix Con Should Print False
"Amazing" Prefix Ame Should  Print False




############## Solution 1 ########################

s="Hello"
suffix="lo"
print(s[-len(suffix):]==suffix)
"""
############ Solution 2 ####################

s="Hello"
suffix="lo"

print(s.endswith(suffix))









