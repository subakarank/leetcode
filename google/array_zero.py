def canTransformToZeroArray(nums, queries):
    n = len(nums)
    diff = [0] * (n + 1)  # Difference array to track range updates
    print(diff)
    
    # Apply each query to the difference array
    for li, ri in queries:
        diff[li] += 1  # Start decrementing at li
        if ri + 1 < n:
            diff[ri + 1] -= 1  # Stop decrementing after ri
    
    print(diff)
    
    # Apply the difference array to simulate decrements
    active_decrements = 0
    for i in range(n):
        active_decrements += diff[i]  # Add active decrements at index i
        print(f"index {i} active decrement {active_decrements}")
        nums[i] -= active_decrements  # Apply decrements to nums[i]
        print(nums[i])
        if nums[i] > 0:  # If any element remains greater than zero, return False
            return False
    
    return True  # If all elements are zero, return True

nums = [1,0,1]
queries = [[0,2]]

print(canTransformToZeroArray(nums, queries))
