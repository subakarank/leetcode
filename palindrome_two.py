'''
https://leetcode.com/problems/valid-palindrome-ii/description/
Given a string s, return true if the s can be palindrome after deleting at most one character from it.
Example 1:

Input: s = "aba"
Output: true
Example 2:

Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.
Example 3:

Input: s = "abc"
Output: false

'''

def palindrome(s: str):
    def is_valid(i, j ):
        while i < j:
            if s[i] != s[j]:
                return False
            else:
                i += 1
                j -= 1
        return True
    def remove_one_char(i, j ):
        return is_valid(i+1, j) or is_valid(i, j - 1)

    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return remove_one_char(left, right)
        else:
            left += 1
            right -= 1
    return True 

print(f'Input: abca output: True {palindrome('abca')}')
print(f'input: abc output: false {palindrome('abc')}')