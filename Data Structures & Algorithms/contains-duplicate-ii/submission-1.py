class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l = 0
        r = 1
        n = len(nums)
        while r < n:
            # print(l,r)
            if nums[l] == nums[r] and r - l <= k:
                # print(l,r)
                return True
            elif r-l >= k:
                l+= 1
                r= l + 1 
            else:
                r+=1
        return False