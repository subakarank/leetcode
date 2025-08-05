print('''
Given two integer lists, nums1 and nums2, of size m and n respectively,
     sorted in nondecreasing order. Merge nums1 and nums2 into a single list sorted in nondecreasing order.
''')

def merge_list(nums1, nums2):
    result = [None] * (len(nums1) + len(nums2))
    p1 = 0
    p2 = 0
    p3 = 0

    while (p1 < len(nums1) and p2 < len(nums2)):
        if nums1[p1] < nums2[p2]:
            result[p3] = nums1[p1]
            p1 += 1
            p3 += 1
        else:
            result[p3] = nums2[p2]
            p2 += 1
            p3 += 1
    while p1 < len(nums1):
        result[p3] = nums1[p1]
        p1 += 1
        p3 += 1
    while p2 < len(nums2):
        result[p3] = nums2[p2]
        p2 += 1
        p3 += 1
    return result

nums1 = [23, 33, 35, 41, 44, 47, 56, 91, 105]
nums2 = [20, 32, 49, 50, 51, 61, 99, 100, 110, 115, 120]
print("Nums1: ", nums1)
print("Nums2: ", nums2)
print("Merged list: ", merge_list(nums1, nums2))

def merge_within_list(nums1: list, nums2: list ):
    p1 = 0
    p2 = 0

    while (p1 < len(nums1) and p2 < len(nums2)):
        if nums1[p1] > nums2[p2]:
            nums1.insert(p1, nums2[p2])
            p1 += 1
            p2 += 1
        else: 
            p1 += 1
    
    if p2 < len(nums2):
        nums1 + nums2[p2:]
    return nums1

nums1 = [23, 33, 35, 41, 44, 47, 56, 91, 105]
nums2 = [20, 32, 49, 50, 51, 61, 99, 100, 110, 115, 120]
print("Nums1: ", nums1)
print("Nums2: ", nums2)
print("Merged list: ", merge_within_list(nums1, nums2))



