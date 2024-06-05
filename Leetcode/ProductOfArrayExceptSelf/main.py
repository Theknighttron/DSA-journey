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
