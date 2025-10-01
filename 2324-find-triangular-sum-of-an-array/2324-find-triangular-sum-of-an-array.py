class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        n = len(nums)
        # print(n)
        if n == 1:
            return nums[0]

        while n > 1:
            newNums = [None] * (n-1)
            for i in range(n - 1):
                # print(nums[i],nums[i+1])
                newNums[i] = (nums[i] + nums[i+1]) % 10
            # print(newNums)
            nums = newNums
            n = len(nums)
        return nums[0]
        