class Solution:

    def encode(self, strs: List[str]) -> str:
        outStr = ""
        for word in strs:
            app = str(len(word)) +'#'+word
            outStr+=app
        return outStr
            
    def decode(self, s: str) -> List[str]:
        lister = []
        index,ranger = 0, len(s)
        while index < ranger:
            j = index
            while s[j] != '#':
                j+=1
            #increment until hit the pound char
            length = int(s[index:j])
            word = s[j+1:j+1+length]
            print(word)
            lister.append(word)
            index = j+1+length
        return lister


