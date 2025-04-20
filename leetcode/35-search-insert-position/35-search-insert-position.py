from typing import List

def searchInsert(nums: List[int], target: int) -> int:
        pfirst = 0
        plast = len(nums) - 1

        while (pfirst <= plast):
            pmiddle = int((plast + pfirst) / 2)
 
            if(nums[pmiddle] == target):
                return pmiddle
            
            if(target < nums[pmiddle]):
                plast = pmiddle - 1
            
            if(target > nums[pmiddle]):
                pfirst = pmiddle + 1
        
        return pfirst

print(searchInsert([1,3], 0))
print(searchInsert([1,3], 1))
print(searchInsert([1,3], 2))
print(searchInsert([1,3,5,6], 9))
print(searchInsert([1,3,5,6], 2))
