class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
         # if not height: return 0

        l, r = 0, len(height)-1
        L, R = height[l], height[r]

        res = 0

# l, r represents the pointer location
# L, R represents the max value on left of l pointer and max value on right of r pointer

        while l<r:
            if L < R:
                l+=1
                L=max(L, height[l])
                res += L - height[l]
            else:
                r-=1
                R=max(R, height[r])
                res += R - height[r]
        return res