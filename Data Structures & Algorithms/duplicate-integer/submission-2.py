class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dicter = {}
        for i in nums:
            if i not in dicter:
                dicter[i] = 1
            else:
                return True
        print(dicter)
        return False