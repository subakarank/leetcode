'''
https://leetcode.com/problems/kth-largest-element-in-an-array/description/

Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?

'''
import random
class Solution:
    def findKthLargest(self, nums, k):
        left, right = 0, len(nums) - 1
        while True:
            pivot_index = random.randint(left, right)
            new_pivot_index = self.partition(nums, left, right, pivot_index)
            if new_pivot_index == len(nums) - k:
                return nums[new_pivot_index]
            elif new_pivot_index > len(nums) - k:
                right = new_pivot_index - 1
            else:
                left = new_pivot_index + 1

    def partition(self, nums, left, right, pivot_index):
        pivot = nums[pivot_index]
        nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
        stored_index = left
        for i in range(left, right):
            if nums[i] < pivot:
                nums[i], nums[stored_index] = nums[stored_index], nums[i]
                stored_index += 1
        nums[right], nums[stored_index] = nums[stored_index], nums[right]
        return stored_index

class Solution: 
    def kth_largest(self, nums: list, k: int):
        left, right = 0 , len(nums)-1
        while True: 
            pivot_index = random.randint(left, right)
            new_pivot_index = self.partition(nums, pivot_index, left, right)
            if new_pivot_index == len(nums) - k:
                return nums[new_pivot_index]
            elif new_pivot_index > len(nums) - k:
                right = new_pivot_index - 1
            else:
                left = new_pivot_index + 1 

    
    def partition(self, nums, pivot_index, left, right):
        pivot = nums[pivot_index]
        nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
        stored_index = 0 
        for i in range(left, right): 
            if nums[i] < pivot: 
                nums[i], nums[stored_index] = nums[stored_index], nums[i]
                stored_index += 1 
        nums[right], nums[stored_index] = nums[right], nums[stored_index]
        return stored_index




    

# # Example usage:
# nums = [3, 2, 1, 5, 6, 4]
# k = 2
# print(find_kth_largest_heap(nums, k))  # Output: 5

# nums = [3,2,1,5,6,4]
# k = 2
# #Output: 5
# print(f"Brute force {find_kth_largest_brute_force(nums, k)}")
# nums = [3,2,3,1,2,4,5,5,6]
# k = 4
# #Output: 4
# print(f"Brute force {find_kth_largest_brute_force(nums, k)}")
