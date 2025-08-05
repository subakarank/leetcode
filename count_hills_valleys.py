def count_hills_and_valleys(nums):
    # Step 1: Remove plateaus
    compressed_nums = []
    for num in nums:
        if not compressed_nums or compressed_nums[-1] != num:
            compressed_nums.append(num)
    
    # Step 2: Count hills and valleys
    hills_and_valleys_count = 0
    n = len(compressed_nums)
    
    for i in range(1, n - 1):
        if (compressed_nums[i] > compressed_nums[i - 1] and compressed_nums[i] > compressed_nums[i + 1]) or \
           (compressed_nums[i] < compressed_nums[i - 1] and compressed_nums[i] < compressed_nums[i + 1]):
            hills_and_valleys_count += 1
            
    return hills_and_valleys_count

# Example usage:
nums = [2, 4, 1, 1, 6, 5]
print(count_hills_and_valleys(nums))  # Output: 2
