nums = [2,0,4,0,9]

def moveZeroess(nums):
    nextNonZero = 0

    for i in range(len(nums)):
        if nums[i] != 0:
            nums[nextNonZero], nums[i] = nums[i], nums[nextNonZero]
            nextNonZero += 1

    print(nextNonZero)

def moveZeroes(nums):
    p1 = 0
    p2 = 1

    while p2 < len(nums):
        num1 = nums[p1]
        num2 = nums[p2]

        if num1 != 0:
            p1 = p1 + 1
            p2 = p2 + 1
        
        elif num1 == 0 and num2 != 0:
            nums[p1] = num2
            nums[p2] = num1
            p1 = p1 + 1
            p2 = p2 + 1
        
        elif num1 == 0 and num2 == 0:
            p2 = p2 + 1

 
    print(nums)

moveZeroess(nums)