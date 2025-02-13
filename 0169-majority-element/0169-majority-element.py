class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Boyer - Moore Algorithm
        count, res = 0, 0
        
        for n in nums:
            if count == 0:
                res = n

            count += (1 if res == n else -1)
        return res




        # T: O(n) S: O(n)
        # res = 0
        # maxCount = 0
        # count = {}

        # for n in nums:
        #     count[n] = 1 + count.get(n, 0)
        #     res = n if count[n]>maxCount else res
        #     maxCount = max(count[n],maxCount)
        # return res