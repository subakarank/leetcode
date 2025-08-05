'''
https://leetcode.com/problems/valid-parentheses/description/
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 
Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
'''

def valid_parentheses(s: str ):
    parentheses = {'(' : ')', '[' : ']', '{' : '}'} 
    stack = []
    for char in s: 
        if char in parentheses:
            stack.append(parentheses[char])
        elif not stack or stack.pop() != char:
            return False
    return not stack

print(f'Input: s = "()" Output: true {valid_parentheses("()")}')
print('Input: s = "()[]{}" Output: true ', end = '')
print(f'{valid_parentheses("()[]{}")}')
print(f'Input: s = "(]" Output: false {valid_parentheses("(]")}')
