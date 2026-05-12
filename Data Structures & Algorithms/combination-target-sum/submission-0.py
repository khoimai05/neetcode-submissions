from typing import List

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        
        def helper(index, cur, sumr):
            if sumr == target:
                res.append(cur[:])  # make a copy
                return
            if sumr > target or index == len(nums):
                return

            cur.append(nums[index])
            helper(index, cur, sumr + nums[index])  # don't increment index
            cur.pop()

            # Skip current number
            helper(index + 1, cur, sumr)
        
        helper(0, [], 0)
        return res
