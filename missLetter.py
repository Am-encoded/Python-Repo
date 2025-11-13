"""
Write a method that takes an array of consecutive (increasing) letters as input and that returns the missing letter in the array.

You will always get a valid array. And it will be always exactly one letter be missing.

The length of the array will always be at least 2.

The array will always contain letters in only one case.

Example:

['a','b','c','d','f'] -> 'e'
['O','Q','R','S'] -> 'P'
"""

def missing_letter(arr):
    for i in range(len(arr)-1):
        if ord(arr[i+1]) - ord(arr[i]) != 1:
            return chr(ord(arr[i])+1)
    return ""
print(missing_letter(['a','b','c','d','f']))
