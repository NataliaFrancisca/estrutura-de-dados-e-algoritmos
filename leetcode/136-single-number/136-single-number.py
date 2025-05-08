numbers = [4,1,2,1,2]

def singleNumber(s):
    result = 0

    for num in s:
        result ^= num

    print(result)

# singleNumber(numbers)
# singleNumber([2,2,1])
# singleNumber([1])
# singleNumber([1,0,1])

print(4^1)
print(5^2)