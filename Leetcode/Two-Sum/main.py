def TwoSum(nums, target):
    result = {}

    # Store the index and corresponding value to the hashmap
    for index, num in enumerate(nums):
        complement = target - num
        
        if complement in result:
           # return the index of the complement from the hashmap 
           # Also return current index  
            return [result[complement], index]
        result[num] = index 


print(TwoSum([2, 7, 11, 15], 9))
print(TwoSum([3, 2, 4], 6))
print(TwoSum([3, 3], 6))

