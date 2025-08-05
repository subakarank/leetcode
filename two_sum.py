# Two Sum
'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

'''

from typing import List

def brute_force_two_sum(lst: List, target: int):
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] + lst[j] == target:
                return[i, j]
    return -1

def two_sum(lst: List, target: int):
    num_to_index = {}
    for key, value in enumerate(lst):
        complement = target - value
        if complement in num_to_index:
            return [num_to_index[complement], key]
        num_to_index[value] = key
    return -1

print("""Brute-force solution""")
print(f"list[2,5,7,4] and target 11: {brute_force_two_sum([2,5,7,4], 11 )}")
print(f"list[2,2,7,4] and target 4: {brute_force_two_sum([2,2,7,4], 4 )}")
print(f"list[2,2,9,4] and target 12: {brute_force_two_sum([2,2,9,4], 12 )}")
print("""Optimised solution solution""")
print(f"list[2,5,7,4] and target 11: {two_sum([2,5,7,4], 11 )}")
print(f"list[2,2,7,4] and target 4: {brute_force_two_sum([2,2,7,4], 4 )}")
print(f"list[2,2,9,4] and target 12: {brute_force_two_sum([2,2,9,4], 12 )}")
