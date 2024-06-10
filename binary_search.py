def brute_force(nums: list[int], target: int) -> int:
    length = len(nums)
    for i in range(length):
        if nums[i] == target:
            return i
    return -1

def recursive(nums, left, right, target):
    if left > right:
        return -1
    mid = (left + right) // 2
    if nums[mid] == target:
        return mid
    elif target > nums[mid]:
        return recursive(nums, mid+1, right, target )
    else:
        return recursive(nums, left, mid-1, target )

def optimised(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right ) // 2 
        if nums[mid] == target:
            return mid
        elif target > nums[mid]:
            left = mid + 1 
        else:
            right = mid - 1
    return -1 

lst = [10, 11, 12, 13, 14, 15, 15, 15, 16, 17, 18, 19, 20]
print(f"it is in the {brute_force(lst, 12)} position")
print(f"it is in the {recursive(lst, 0, len(lst)-1, 12)} position")
print(f"it is in the {optimised(lst, 12)} position")

print('-' * 60 )
lst = [5]
print(f"it is in the {brute_force(lst, 5)} position")
print(f"it is in the {recursive(lst, 0, len(lst)-1, 5)} position")
print(f"it is in the {optimised(lst, 5)} position")

