"""
📌 Description:
Write a Python program that checks if the string s contains all the letters in the alphabet (case-insensitive, so "A" should be equivalent to "a").

If it does, print True. Else, print False.

Before comparing the characters, you should convert the string to lowercase.

If the string contains spaces, ignore them before finding the result.

You may assume that the string doesn't contain any other symbols, only spaces (possibly).

Consider these letters as part of the alphabet: 'abcdefghijklmnopqrstuvwxyz

📌 Output:
'abcdefghijklmnopqrstuvwxyz Print out True
"The quick brown fox jumps over lazy dog"  Print out True
"Hello" Print out False

############ Solutions  1 ##################
import string
s="hello"
space=""
# Convert String into sets because set do not have duplicate elements
s_set= set(s.lower())
# Remove space on set if precense
if space in s_set:
  s_set.remove(" ")
#ascii_lowercase represent all alphabet in numbeer presence
print(s_set==set(string.ascii_lowercase))

"""

############ Solution 2 ##################

import string
s="The quick brown fox jumps over the lazy dog"
is_pangram=True

for char in string.ascii_lowercase:
    if char not in  s.lower():
        is_pangram=False
        break
print(is_pangram)











