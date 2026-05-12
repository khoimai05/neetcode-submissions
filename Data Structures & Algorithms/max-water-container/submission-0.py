class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max = 0
        r,l = 0, len(heights) - 1
        while l>r:
            val = min(heights[l], heights[r])*(l-r)
            if val > max:
                max = val
            if min(heights[l], heights[r]) == heights[l]:
                l = l-1
            else:
                r = r+1 
        return max
