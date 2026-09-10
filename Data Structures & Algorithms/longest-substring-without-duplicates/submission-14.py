class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}  # char -> last index seen
        L = 0
        res = 0

        for R in range(len(s)):
            if s[R] in seen and seen[s[R]] >= L:
                L = seen[s[R]] + 1  # jump past the stale/duplicate occurrence
            seen[s[R]] = R
            res = max(res, R - L + 1)

        return res