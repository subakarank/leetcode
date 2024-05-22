#Two Sum
'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
'''

from typing import List

def brute_force_two_sum(lst: List, target: int):
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] + lst[j] == target:
                return[i, j]
    return -1

def two_sum(lst: List, target: int):
    list_to_dict = {}
    for key, value in enumerate(lst):
        list_to_dict[value] = key
    for i in range(len(lst)):
        complement = target - lst[i] 
        if complement in list_to_dict and i != list_to_dict[complement]:
            return [i, list_to_dict[complement]]
    return -1


print("""Brute-force solution""")
print(f"list[2,5,7,4] and target 11: {brute_force_two_sum([2,5,7,4], 11 )}")
print(f"list[2,2,7,4] and target 4: {brute_force_two_sum([2,2,7,4], 4 )}")
print(f"list[2,2,9,4] and target 12: {brute_force_two_sum([2,2,9,4], 12 )}")
print("""Optimised solution solution""")
print(f"list[2,5,7,4] and target 11: {two_sum([2,5,7,4], 11 )}")
print(f"list[2,2,7,4] and target 4: {brute_force_two_sum([2,2,7,4], 4 )}")
print(f"list[2,2,9,4] and target 12: {brute_force_two_sum([2,2,9,4], 12 )}")

