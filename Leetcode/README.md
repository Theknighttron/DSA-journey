## Two Sum 

### Problem Description:
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
> You may assume that each input would have exactly one solution, and you may not use the same element twice.
> You can return the answer in any order.

##### The Intuition
1. Iterate over the List
2. Find the complement of the current element
3. Check if the complement exist in our hashmap
4. Return the indices if found
5. If not found update the hashmap by adding the current number with it's index

```
def TwoSum(nums, target):
    result = {}

    for index, num in enumerate(nums):
        complement = target - num
        
        if complement in result:
            return [result[complement], i]
        result[num] = index
``` 


Time complexity: O(n)
Space Complexity: O(n)
