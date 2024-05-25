'''
Given the root node of a binary search tree and two integers low and high, 
return the sum of values of all nodes with a value in the inclusive range [low, high].
'''

from typing import List

def range_sum_brute_force(nums: List, low: int, high: int) -> int:
    sum = 0 
    while low <= high: 
        if low in nums:
            sum += low
        low += 1
    return sum 

    