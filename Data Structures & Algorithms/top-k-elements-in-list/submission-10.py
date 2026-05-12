class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:    
        dicter = {}
        for i in nums:
            if i in dicter:
                dicter[i] += 1
            else:
                dicter[i] = 1
        print(dicter)
        lister = []
        while k >= 1:
            max = 0
            for i, j in dicter.items():
                if j >= max:
                    max = j
            
            for a,b in dicter.items():
                if b == max:
                    lister.append(a)
                    break
            del(dicter[lister[-1]])
            k = k  - 1
        return lister
        