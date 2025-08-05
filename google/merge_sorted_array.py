def merge_sorted_array(nums1: list, m: int, nums2: list, n: int): 
    p1 = m - 1
    p2 = n - 1
    p = m + n - 1

    while p1 >= 0 and p2 >= 0: 
        if nums1[p1] > nums2[p2]: 
            nums1[p] = nums1[p1]
            p1 -= 1
            
        else: 
            nums1[p] = nums2[p2]
            p2 -=1 
        p -= 1

    while p2 >= 0:
        nums1[p] = nums2[p2]
        p2 -= 1
        p -= 1

nums1 = [0]
nums2 = [1]
merge_sorted_array(nums1, 0, nums2 , 1)
print(nums1)
