''''
https://leetcode.com/problems/missing-ranges/description/

You are given an inclusive range [lower, upper] and a sorted unique integer array nums, where all elements are within the inclusive range.
A number x is considered missing if x is in the range [lower, upper] and x is not in nums.
Return the shortest sorted list of ranges that exactly covers all the missing numbers.
That is, no element of nums is included in any of the ranges, and each missing number is covered by one of the ranges.

'''

def find_missing_range(nums: list, lower: int, upper: int): 
    missing_range = []
    current = lower

    for num in nums:
        if num > current:
            if current == num-1:
                missing_range.append([current, current])
            else:
                missing_range.append([current, num-1])
        current = num + 1 
    
    if current <= upper:
        if current == upper -1:
            missing_range.apped([current, current])
        else:
            missing_range.append([current, upper])
    
    return missing_range

    
print(f"Input: nums = [0,1,3,50,75], lower = 0, upper = 99 : Output: [[2,2],[4,49],[51,74],[76,99]]:  {find_missing_range([0,1,3,50,75], 0, 99)}")
print(f"Input: nums = [-1], lower = -1, upper = -1 : Output: []:  {find_missing_range([-1], 0, 99)}")


