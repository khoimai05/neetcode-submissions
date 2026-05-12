class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def helper(i, nums, sub, cur):
            if i == len(nums):
                sub.append(cur.copy())
                return
            # Include nums[i]
            cur.append(nums[i])
            helper(i + 1, nums, sub, cur)
            # Exclude nums[i]
            cur.pop()
            helper(i + 1, nums, sub, cur)
        
        sub, cur = [], []
        helper(0, nums, sub, cur)
        return sub