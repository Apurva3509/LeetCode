class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        maxCount = 0
        count = {}

        for n in nums:
            count[n] = 1 + count.get(n, 0)
            res = n if count[n]>maxCount else res
            maxCount = max(count[n],maxCount)
        return res