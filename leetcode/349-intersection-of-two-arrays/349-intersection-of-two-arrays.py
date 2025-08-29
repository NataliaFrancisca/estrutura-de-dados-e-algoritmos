nums1 = [1,2,2,1]
nums2 = [2,2]

nums4 = [4,9,5]
nums5 = [9,4,9,8,4]

def intersection(nums1, nums2):
    seen = {}
    dumb = []

    for num in nums1:
        seen[num] = 1

    for num in nums2:
        if seen.get(num) == 1:
            seen[num] = 2
            dumb.append(num)

    return dumb

# this works but it's not good.
# def intersection(nums1, nums2):
#     dictionary = {}
#     dumb = []

#     for num in nums1:
#         count = 0

#         while count < len(nums2):
#             if num == nums2[count]:
#                 if dictionary.get(num) is None:
#                     dictionary[num] = True
#                     dumb.append(num)

#                 count = 0
#                 break
#             count = count + 1

#         count = 0;

#     print(dumb)

a = intersection(nums1, nums2)
b = intersection(nums4, nums5);

print(a)
print(b)