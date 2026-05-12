class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        dicter = {}
        maxer = 0
        l = 0

        for r in range(len(s)):
            while s[r] in dicter:
                del dicter[s[l]]
                l += 1
            dicter[s[r]] = 1
            maxer = max(maxer, r - l + 1)

        return maxer
