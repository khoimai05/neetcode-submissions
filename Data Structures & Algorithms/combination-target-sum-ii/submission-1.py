from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        nums = candidates
        res = []
        
        def helper(index, cur, sumr):
            if sumr == target:
                res.append(cur[:])  # make a copy
                return
            if sumr > target or index == len(nums):
                return

            cur.append(nums[index])
            helper(index+1, cur, sumr + nums[index])  # don't increment index
            cur.pop()
            while index + 1 <len(nums) and nums[index] == nums[index+1]:
                index+=1
            # Skip current number
            helper(index + 1, cur, sumr)
        
        helper(0, [], 0)
        return res
