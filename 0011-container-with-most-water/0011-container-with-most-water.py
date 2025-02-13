class Solution(object):
    def maxArea(self, heights):
        """
        :type height: List[int]
        :rtype: int
        """

        l, r = 0, len(heights)-1
        vol = 0

        while l<r:
            area = (r-l)*min(heights[l],heights[r])
            vol = max(vol, area)

            if heights[l]<heights[r]:
                l+=1
            elif heights[l]>heights[r]:
                r-=1
            # else:
            #     max(heights[r],heights[l])
            else:
                l+=1
        return vol
        