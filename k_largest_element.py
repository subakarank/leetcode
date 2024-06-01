'''
https://leetcode.com/problems/kth-largest-element-in-an-array/description/

Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?

'''
import heapq

def find_kth_largest_brute_force(nums: list[int], k: int): 
    return sorted(nums, reverse=True)[k-1]

def find_kth_largest_heap(nums, k):
    # Initialize a min-heap with the first k elements of the array
    min_heap = nums[:k]
    heapq.heapify(min_heap)
    print(f"Initial heap after heapify with first {k} elements: {min_heap}")

    
    # Iterate over the rest of the elements in the array
    for num in nums[k:]:
        # If the current number is larger than the smallest in the heap
        if num > min_heap[0]:
            heapq.heappop(min_heap)
            print(min_heap)
            heapq.heappush(min_heap, num)
            print(min_heap)
    
    # The root of the heap (smallest element in the heap) is the k-th largest element
    return min_heap[0]

import random

def partition(nums, left, right):
    pivot_index = random.randint(left, right)
    pivot = nums[pivot_index]
    nums[pivot_index], nums[right] = nums[right], nums[pivot_index]  # Move pivot to end
    store_index = left
    for i in range(left, right):
        if nums[i] > pivot:  # We want the largest k, so we use `>` here for max-heap behavior
            nums[store_index], nums[i] = nums[i], nums[store_index]
            store_index += 1
    nums[store_index], nums[right] = nums[right], nums[store_index]  # Move pivot to its final place
    return store_index

def quickselect(nums, left, right, k):
    if left == right:
        return nums[left]
    
    pivot_index = partition(nums, left, right)
    
    # The pivot is in its final sorted position
    if k == pivot_index:
        return nums[k]
    elif k < pivot_index:
        return quickselect(nums, left, pivot_index - 1, k)
    else:
        return quickselect(nums, pivot_index + 1, right, k)

def find_kth_largest(nums, k):
    # k-1 because we need to convert k from 1-based index to 0-based index
    return quickselect(nums, 0, len(nums) - 1, k - 1)

# Example usage:
nums = [3, 2, 1, 5, 6, 4]
k = 2
print(find_kth_largest(nums, k))  # Output: 5



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
