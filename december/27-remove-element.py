def removeElement(nums, target):
    nextNonTarget = 0
    size = 0

    for i in range(len(nums)):
        if nums[i] != target:
            nums[i], nums[nextNonTarget] = nums[nextNonTarget], nums[i]
            nextNonTarget += 1
            size += 1  
        print("nums", nums)

    print(nums)
    print(size)


# removeElement([3,2,2,3], 3)
removeElement([0,1,2,2,3,0,4,2], 2)