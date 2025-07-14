def containsDuplicate(nums):
    dictionary = {}

    for num in nums:
        if dictionary.get(num) is None:
            dictionary[num] = True
        else:
            return True

    return False

a = containsDuplicate([1,2,3])
print(a)