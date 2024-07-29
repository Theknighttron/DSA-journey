class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        res  = 0
        counts = {}

        for n in nums:
            if n in counts:
                res = res + counts[n]
                counts[n] = counts[n] + 1
            else:
                counts[n] = 1
        return res
