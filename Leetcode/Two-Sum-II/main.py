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
