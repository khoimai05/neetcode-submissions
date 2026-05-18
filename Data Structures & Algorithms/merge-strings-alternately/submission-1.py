class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        fi = 0
        se = 0
        res = ''
        while fi < len(word1) and se < len(word2):
            res += word1[fi]
            res += word2[se]
            fi+=1
            se+=1
        if fi == len(word1):
            res += word2[se:]
        if se == len(word2):
            res += word1[fi:]
        return res