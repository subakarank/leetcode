'''
Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution,
 and you may not use the same element twice.

You can return the answer in any order. 

Input: nums = [2,7,11,15], target = 9
[0, 1 ]

9 - 2 = 7 

[3, 4, 6]  = 10 
 - data structure: Disctionary 
'''

def two_sums(nums: list, target: int) -> list: 
    store = {}
    for i in range(len(nums)): 
        compliment = target - nums[i] # 10 - 3 = 7 , 10 -4 = 6, 10 - 6 = 4 
        if compliment in store: 
            return [ store[compliment], i ] # [1, 2  ]
        else: 
            store[nums[i]] = i  # {'3': 0, '4': 1  }

print(two_sums([3, 4, 6], 10))

# Time complexity 
# Space complexity 
        


    



 




