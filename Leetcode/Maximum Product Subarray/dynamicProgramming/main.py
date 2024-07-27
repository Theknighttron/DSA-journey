def maxProduct(self, nums: List[int]) -> int:
    result = max(nums)
    currentMin, currentMax = 1, 1

    for n in nums:
        if n == 0:
            currentMin, currentMax = 1, 1
            continue

        tmp = currentMax * n
        currentMax = max(n, n * currentMax, n * currentMin)
        currentMin = min(n, tmp, n * currentMin)
        result = max(result, currentMax)

    return result


