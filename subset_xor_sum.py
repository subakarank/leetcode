def xor_sum(nums: list):
    n = len(nums)
    total_sum  = 0
    for i in range(1 << n):
        subset_xor = 0
        for j in range(n):
            if i & (1 << j):
                subset_xor ^= nums[j]
        total_sum += subset_xor
    return total_sum

def subset_xor_sum_recursive(self, nums: list[int]) -> int:
    def dfs(index, current_xor):
        # Base case: when all elements have been considered
        if index == len(nums):
            return current_xor
        # Include nums[index] in the subset
        include = dfs(index + 1, current_xor ^ nums[index])
        # Exclude nums[index] from the subset
        exclude = dfs(index + 1, current_xor)
        return include + exclude
    
    return dfs(0, 0)