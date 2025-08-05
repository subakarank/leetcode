# https://leetcode.com/problems/remove-invalid-parentheses/description/
'''
Given a string s that contains parentheses and letters, remove the minimum number of invalid parentheses to make the input string valid.
Return a list of unique strings that are valid with the minimum number of removals. You may return the answer in any order.

'''

def is_valid(s):
    count = 0
    for char in s:
        if char == '(':
            count += 1
        elif char == ')':
            count -= 1
            if count < 0:
                return False
    return count == 0

def removeInvalidParentheses(s):
    if not s:
        return [""]
    
    queue = [s]
    visited = set([s])
    found = False
    result = []
    front = 0  # pointer to track the front of the queue
    
    
    while front < len(queue):
        current = queue[front]
        front += 1
        
        if is_valid(current):
            result.append(current)
            found = True
        
        if found:
            continue
        # Generate all possible strings by removing one parenthesis
   
        for i in range(len(current)):
            if current[i] in '()':
                new_str = current[:i] + current[i+1:]
                if new_str not in visited:
                    visited.add(new_str)
                    queue.append(new_str)
        print(queue)
    
    return result

# Input: s = "()())()"
print(f" input = '()())()' Expecting : ['(())()','()()()']  Output {removeInvalidParentheses('()())()')}")
