class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temp = temperatures
        res = [0]*len(temp)
        i = 0
        while i < len(temp):
            check = False
            warm = 0
            for j in range(i+1,len(temp)):
                if temp[i] >= temp[j]:
                    warm+=1
                else:
                    warm+=1
                    res[i] = warm
                    break
            i = i + 1
        return res
        