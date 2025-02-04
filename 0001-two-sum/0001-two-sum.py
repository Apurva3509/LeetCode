class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}
        
        for i in range(len(nums)):
            n = nums[i]
            val = target - n
            if val in seen:
                return [seen[val], i]
            seen[n] = i
        
        return []

        