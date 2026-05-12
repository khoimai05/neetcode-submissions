class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ptr = 0
        setter = set()
        for a in s1:
            setter.add(a)
        for i in range(ptr, len(s2)):  
            if s2[i] not in setter:
                continue
            else:
                ex = s2[i:i+len(s1)]
                print(ex)
                if (sorted(ex) == sorted(s1)):
                    return True
                else:
                    continue
        return False