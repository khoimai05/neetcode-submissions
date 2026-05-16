class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        res = 0

        for n in numSet:
            if (n - 1) not in numSet:
                streak = 0
                curr = n
                while curr in numSet:
                    streak += 1
                    curr += 1
                res = max(res, streak)
        return res