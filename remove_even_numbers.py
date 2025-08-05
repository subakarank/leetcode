def remove_even(nums: list):
    results = []
    for num in nums:
        if num % 2 != 0:
            results.append(num)
    return results

def remove_even_comprehension(nums: list):
    return [num for num in nums if num % 2 != 0]

nums = [3, 2, 41, 3, 34]
print("remove_even [3, 2, 41, 3, 34]:", remove_even(nums))
print("remove_even_comprehension [3, 2, 41, 3, 34]:", remove_even_comprehension(nums))

print("-" * 100 )

nums = [-5, -4, -3, -2, -1]
print("remove_even [-5, -4, -3, -2, -1]:", remove_even(nums))
print("remove_even_comprehension [-5, -4, -3, -2, -1]:", remove_even_comprehension(nums))

print("-" * 100 )

nums = [1, 2, 3, 7]
print("remove_even [1, 2, 3, 7]:", remove_even(nums))
print("remove_even_comprehension [1, 2, 3, 7]:", remove_even_comprehension(nums))


