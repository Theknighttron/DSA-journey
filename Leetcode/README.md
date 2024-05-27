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



