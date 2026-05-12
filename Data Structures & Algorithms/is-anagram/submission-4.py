class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_dict  = {}
        t_dict = {}
        for s_char in s:
            if s_char in s_dict:
                s_dict[s_char] += 1
                continue
            s_dict[s_char] = 1
        for t_char in t:
            if t_char in t_dict:
                t_dict[t_char] += 1
                continue
            t_dict[t_char] = 1
        
        return s_dict  == t_dict
