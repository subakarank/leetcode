'''
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
'''

def palindrome(s:str) -> bool:
    s.re
    new_string = ''.join([char.lower() for char in s if char.isalnum() ])
    return new_string == new_string[::-1]


def palindrome_sub_optimal(s: str):
    new_string = ''.join([char.lower() for char in s if char.isalnum() ])
    left = 0
    right = len(new_string) -1
    while left < right:
        if(new_string[left] != new_string[right]):
            return False
        left += 1
        right -= 1
    return True

def palindrome_sub_optimal_1(s: str):
    left = 0
    right = len(s) -1
    while left < right:
        skip = False
        if ignore_char(s[left]) :
            left += 1
            skip = True
        if ignore_char(s[right]) :
            right -= 1
            skip = True 
        if skip:
            continue 

        if (s[left].lower() != s[right].lower()):
            return False
        left += 1
        right -= 1
    return True

def ignore_char(value: str)->bool: 
    if not (65 <= ord(value) <= 90 or 97 <= ord(value) <= 122) :
        return True
    else: 
        return False 

print(palindrome('madam'))
print(palindrome_sub_optimal('ma   dam'))

print(palindrome('A man, a plan, a canal: Panama'))
print(palindrome_sub_optimal('A man, a plan, a canal: Panama'))

print("madam palindrome_sub_optimal_1", palindrome_sub_optimal_1('madam'))
print("A man, a plan, a canal: Panama palindrome_sub_optimal_1", palindrome_sub_optimal_1('A man, a plan, a canal: Panama'))