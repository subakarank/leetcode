'''
You are given two integer arrays nums1 and nums2 of sizes n and m, respectively. Calculate the following values:

answer1 : the number of indices i such that nums1[i] exists in nums2.
answer2 : the number of indices i such that nums2[i] exists in nums1.

Input: nums1 = [2,3,2], nums2 = [1,2]

Output: [2,1]


Example 2:

Input: nums1 = [4,3,2,3,1], nums2 = [2,2,5,2,3,6]

Output: [3,4]

Explanation:

The elements at indices 1, 2, and 3 in nums1 exist in nums2 as well. So answer1 is 3.

The elements at indices 0, 1, 3, and 4 in nums2 exist in nums1. So answer2 is 4.
'''

def intersection_elements(nums1: list, nums2: list):
    nums1_count = 0
    nums2_count = 0
    for num in nums1:
        if num in nums2:
            nums1_count += 1
    for num in nums2:
        if num in nums1:
            nums2_count += 1
    return [nums1_count, nums2_count]

def intersection_elements_(nums1: list, nums2: list):
    counts = [0,0]
    set_nums2 = set(nums2)
    set_nums1 = set(nums1)
    
    for num in nums1:
        if num in set_nums2:
            counts[0] += 1
    for num in nums2:
        if num in set_nums1:
            counts[1] += 1
    return counts

def intersection_elements_2(nums1: list, nums2: list):
    set1 = set(nums1)
    set2 = set(nums2)

    # Count the occurrences in each direction
    count1 = sum(num in set2 for num in nums1)
    count2 = sum(num in set1 for num in nums2)

    return [count1, count2]
