
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)        
        nums = sorted(nums)
        print(nums)
        if len(nums) <= 1:
            return len(nums)
        l=0
        r=1
        res = 1
        while r != len(nums):
            if nums[r] != nums[r-1] + 1:
                print(f"{nums[l]} and {nums[r]}")
                l=r
                r=r+1
            else:
                res = max(res,r-l+1)
                r = r + 1
        return res