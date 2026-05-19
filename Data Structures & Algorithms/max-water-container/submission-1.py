class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        res = 0
        while l < r:
            print(f'{r} - {l}')
            max_area = min(heights[l],heights[r])*(r-l)
            print(max_area)
            res = max(res,max_area)
            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1
        return res