class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        fi = 0 
        sec = 0
        res =''
        filen = len(word1)
        seclen = len(word2)
        while fi < filen and sec < seclen:
            res += word1[fi]
            res += word2[sec]
            fi+=1
            sec+=1
        if fi == filen:
            res += word2[sec:]
        if sec == seclen:
            res+= word1[fi:]
        return res
        