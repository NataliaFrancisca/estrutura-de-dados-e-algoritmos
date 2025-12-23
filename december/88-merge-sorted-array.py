# 22 - 12 - 2025
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

def merge(nums1, m, nums2, n):
    end = m + n - 1
    p1 = m - 1
    p2 = n - 1

    while p2 >= 0:
        if p1 >= 0 and nums1[p1] > nums2[p2]:
            nums1[end] = nums1[p1]
            p1 -= 1
        else:
            nums1[end] = nums2[p2]
            p2 -= 1
        
        end -= 1

    print(p1, end)
    return nums1

a = merge(nums1, m, nums2, n)
print(a)