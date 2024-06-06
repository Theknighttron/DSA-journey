def maximumSubarray(nums):
    max_current = nums[0]
    max_global = nums[0]

    for i in range(1, len(nums)):
        max_current = max(nums[i], max_current + nums[i])

        if max_current > max_global:
            max_global = max_current

    return max_global

input = [-2, 3, 2, -1]
print(maximumSubarray(input))
