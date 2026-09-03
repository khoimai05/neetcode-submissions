class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def quicksort(unsorted):
            if len(unsorted) == 1:
                return unsorted
            lent = len(unsorted)//2
            a = quicksort(unsorted[0:lent])
            b = quicksort(unsorted[lent:])
            res = []
            i,j =0,0
            while i < len(a) and j < len(b):
                if a[i] < b[j]:
                    res.append(a[i])
                    i+=1
                else:
                    res.append(b[j])
                    j+=1
            if i < len(a):
                res.extend(a[i:])
            if j < len(b):
                res.extend(b[j:])
            return res
        return quicksort(nums)

