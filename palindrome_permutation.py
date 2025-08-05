'''
https://leetcode.com/problems/palindrome-permutation/description/
Given a string s, return true if a permutation of the string could form a 
palindrome
 and false otherwise.
'''
from collections import Counter
def palindrome_permutation(s:str) -> bool: 
    char_count = {char: s.count(char) for char in s } 
    odd_count = sum(1 for value in char_count.values() if value % 2 != 0 )
    if odd_count <= 1:
        return True
    return False 

# Example usage:
s = "aab"
print(palindrome_permutation(s))  # Output: True

s = "carerac"
print(palindrome_permutation(s))  # Output: True

s = "code"
print(palindrome_permutation(s))  # Output: False