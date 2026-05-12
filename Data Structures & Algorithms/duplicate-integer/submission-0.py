class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i, val_i in enumerate(nums):
            for j, val_j in enumerate(nums):
                if i == j:
                    continue;
                if val_i == val_j:
                    return True
        
        return False
                
         