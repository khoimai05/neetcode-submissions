class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        L = 0
        n = len(s)
        res = 0
        dicter = {}
        R=0
        for R in range(n):
            max_key = 0
            dicter[s[R]] = dicter.get(s[R],0) + 1
            max_val = 0
            for key, val in dicter.items():
                if val > max_val:                    
                    max_val = val
                    max_key = key
            window_size = R-L+1
            if window_size - max_val > k:
                dicter[s[L]] -=1
                L+=1
            else:
                res = max(res, window_size)
        return res 