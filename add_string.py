'''
https://leetcode.com/problems/add-strings/description/

Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.

You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.

 

Example 1:

Input: num1 = "11", num2 = "123"
Output: "134"


'''

def add_strings(num1: str, num2: str) -> str:
    result = '' 
    carry = 0
    i = len(num1) - 1 
    j = len(num2) - 1

    while i >= 0 or j >= 0 or carry: 
        digit1 = int(num1[i]) if i >= 0 else 0
        digit2 = int(num2[j]) if j >= 0 else 0

        total = digit1 + digit2 + carry
        result += str( total % 10 ) 
        carry = total // 10
        i -= 1 
        j -= 1

    return result[::-1]

def add_strings2(num1: str, num2: str) -> str:
    result = '' 
    carry = 0
    i = len(num1) - 1 
    j = len(num2) - 1

    while i >= 0 or j >= 0 or carry: 
        digit1 = ord(num1[i]) - ord('0') if i >= 0 else 0
        digit2 = ord(num2[j]) - ord('0')  if j >= 0 else 0

        total = digit1 + digit2 + carry

        result += chr( total % 10  + ord('0'))
        carry = total // 10
        i -= 1 
        j -= 1

    return result[::-1]
print(f'add_strings : Input: num1 = "11", num2 = "123" Output: "134" : {add_strings('11', '123')}')
print(f'add_strings : Input: num1 = "456", num2 = "77" Output: "533" : {add_strings('456', '77')}')

print('-' * 60 )
print(f'add_strings2 : Input: num1 = "11", num2 = "123" Output: "134" : {add_strings2('11', '123')}')
print(f'add_strings2 : Input: num1 = "456", num2 = "77" Output: "533" : {add_strings2('456', '77')}')

