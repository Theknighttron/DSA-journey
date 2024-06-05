## 1. Two Sum

### Problem Description:

> Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
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


Time Complexity: O(n) <br>
Space Complexity: O(n)



## 2. Best Time to Buy and Sell Stocks

### Problem Description:

> You are given an array prices where prices[i] is the price of a given stock on the ith day.
> You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
> Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

##### The Intuition
1. Iterate over the list of all given prices
2. Check for lower buy price
3. Calculate and Update the maximum profit
4. Return the maximum profit


```
def MaxProfit(prices):
    buy = [0]
    profit = 0


    for price in prices:
        if price < buy:
            buy = price
        elif price - buy > profit:
            profit = price - buy
    return profit
```


Time Complexity: O(n) <br>
Space Complexity: O(1)


## 3. Two Sum II - Input Array Is Sorted

### Problem Description:
> Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order,
> find two numbers such that they add up to a specific target number.
> Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
> Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.
> The tests are generated such that there is exactly one solution. You may not use the same element twice.
> Your solution must use only constant extra space.


##### The Intuition
1. Pointer initializiation, one to point to the start and other to the end of the given array.
2. Loop through the array as long as the leftPointer is less than the rightPointer
3. Find the sum of the left and right  element at current indexes position
4. Condition to adjust the pointer based on the sum and the target
5. Return the index of element that sum's up to the target plus one



```
def TwoSum(numbers, target):
    leftPointer = 0
    rightPointer = len(numbers) - 1

    while leftPointer < rightPointer:
        sum = numbers[leftPointer] + numbers[rightPointer]

        if sum > target:
            rightPointer -= 1
        elif sum < target:
            leftPointer += 1
        else:
            return [leftPointer + 1, rightPointer + 1]


arr = [2, 7, 11, 15]
print(TwoSum(arr, 9))
```



## 4. Contains Duplicate


### Problem Description:

> Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct

##### The Intuition



```
def containsDuplicate(nums):
    seen = set()

    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

numbers = [1, 2, 3, 1]
print(containsDuplicate(numbers))
```

Time Complexity: O(n) <br>
Space Complexity: O(n)

## 5. Product Array Except Self


### Problem Description:

> Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
> The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
> You must write an algorithm that runs in O(n) time and without using the division operation.


##### The Intuition



```
def productExceptSelf(nums):
    answer = [1] * len(nums)

    left = 1
    right = 1


    for i in range(len(nums)):
        answer[i] = left
        left = left * nums[i]
    for i in range(len(nums) -1, -1, -1):
        answer[i] *= right
        right = right * nums[i]
    return answer

numbers = [1, 2, 3, 4]
print(productExceptSelf(numbers))
```

Time Complexity: O(n) <br>
Space Complexity: O(n)
