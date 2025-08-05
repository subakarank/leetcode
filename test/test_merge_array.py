
def merge_array(nums1: list, m: int, nums2: list, n: int ):
    p1 = m - 1
    p2 = n - 1
    p = m + n - 1

    while p1 >= 0 and p2 >= 0:
        if nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1 
        p -= 1
    
    while p2 >= 0:
        nums1[p] = nums2[p2]
        p2 -= 1
        p -= 1
    return nums1

class TestMergeArray():
    def test_merge_array_case1(self):
        nums1 = [1,2,3,0,0,0]
        nums2 = [2,5,6]
        m = 3
        n = 3
        merge_array(nums1, 3, nums2, n)
        assert nums1 == [1, 2, 2, 3, 5, 6]

