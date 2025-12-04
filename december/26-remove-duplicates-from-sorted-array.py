nums = [0,0,1,1,1,2,2,3,3,4]

def removeDuplicates(nums):
    if not nums:
        return 0
    
    write = 0

    for read in range(1, len(nums)):
        if nums[read] != nums[write]:
            write += 1
            nums[write] = nums[read]

    return nums

a = removeDuplicates(nums)
print(a)