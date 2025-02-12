class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # we can reverse the entire array, reverse the first k elements and then the remaining to get rotated array
        # nums = [1 2 3 4 5 6 7]; k = 3
        # Step 1 reverse: nums = [7 6 5 4 3 2 1]
        # Step 2 reverse first k(3): nums = [5 6 7 4 3 2 1] 
        # Step 3 reverse remaining: nums = [5 6 7 1 2 3 4] --> rotated array

        # if k = 4 and len)nums= 4, effective rotation is null, 
        # also if k = 7 and len(nums) = 5, we have to rotate by only 2

        k = k % len(nums) 
        # step 1
        l, r = 0, len(nums) - 1
        while l<r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

        # step 2
        l, r = 0, k - 1
        while l<r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

        # step 3
        l, r = k, len(nums) - 1
        while l<r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

        