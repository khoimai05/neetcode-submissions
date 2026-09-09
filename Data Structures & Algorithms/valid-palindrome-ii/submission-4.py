class Solution:
    def validPalindrome(self, s: str) -> bool:
        l,r = 0, len(s) - 1
        once = True
        while l < r:
            if s[l] == s[r]:
                l = l+1
                r = r-1
            else:
                break   
            
        first = s[l+1:r+1]
        second = s[l:r]
        if first == first[::-1] or second == second[::-1]:
                    return True
        return False
 