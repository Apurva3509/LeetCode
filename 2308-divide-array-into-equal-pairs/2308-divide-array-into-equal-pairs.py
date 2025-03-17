class Solution(object):
    def divideArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        vals = Counter(nums)
        print(vals)

        for val in vals.values():
            if val%2 != 0:
                return False
        return True