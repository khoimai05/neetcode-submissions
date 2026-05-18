class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue                  # skip dup anchor
            if nums[i] > 0:
                break                     # smallest is positive → done
            l, r, target = i + 1, n - 1, -nums[i]
            while l < r:
                s = nums[l] + nums[r]
                if s == target:
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l+1]: l += 1   # skip dup l
                    while l < r and nums[r] == nums[r-1]: r -= 1   # skip dup r
                    l += 1
                    r -= 1
                elif s < target:
                    l += 1
                else:
                    r -= 1
        return res