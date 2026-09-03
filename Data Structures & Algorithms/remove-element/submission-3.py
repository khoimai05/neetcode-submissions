class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # 'k' tracks the index where the next non-val element should go
        k = 0  
        
        for i in range(len(nums)):
            # If the current element is not the value to remove
            if nums[i] != val:
                # Move it to the front of the list at index k
                nums[k] = nums[i]
                # Move the pointer forward
                k += 1
                
        return k
