
'''
https://leetcode.com/problems/fibonacci-number/description/
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.

Given n, calculate F(n).
Example 1:

Input: n = 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.

Example 2:

Input: n = 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.

Example 3:

Input: n = 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.

'''

def fib_recursive(n):
    if n <=1 :
        return n
    else: 
        return fib_recursive(n-1) + fib_recursive(n-2)

print(f" fib_recursive(2) Expecting: 1: Output: {fib_recursive(2)}")
print(f" fib_recursive(3) Expecting: 2: Output: {fib_recursive(3)}")
print(f" fib_recursive(4) Expecting: 4: Output: {fib_recursive(4)}")
print('-' * 60)

def fib_recursive_memoized(n, memo={}):
    if n <=1 :
        return n
    if n not in memo:
        memo[n] = fib_recursive_memoized(n-1, memo) + fib_recursive_memoized(n-2, memo )
    return memo[n]

print(f" fib_recursive_memoized(2) Expecting: 1: Output: {fib_recursive_memoized(2)}")
print(f" fib_recursive_memoized(3) Expecting: 2: Output: {fib_recursive_memoized(3)}")
print(f" fib_recursive_memoized(4) Expecting: 4: Output: {fib_recursive_memoized(4)}")
print('-' * 60)

def fib_optimised(n):
    if n <=1 :
        return n
    prev, current = 0, 1
    for _ in range(2, n + 1):
        prev, current = current, prev + current
    
    return current

print(f" fib_optimised(2) Expecting: 1: Output: {fib_optimised(2)}")
print(f" fib_optimised(3) Expecting: 2: Output: {fib_optimised(3)}")
print(f" fib_optimised(4) Expecting: 4: Output: {fib_optimised(4)}")
    



