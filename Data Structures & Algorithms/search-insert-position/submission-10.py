class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l,r = 0,len(nums) - 1
        while l<=r:
            # print(nums[l:r+1])
            mid = l + (r-l)//2
            if target == nums[mid]:
                return mid
            if target > nums[mid]:
                if mid+1 == len(nums):
                    return mid+1
                if target <= nums[mid+1]:
                    return mid +1
                l = mid + 1
            if target < nums[mid]:
                r = mid -1
        return mid