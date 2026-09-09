class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        i  = 1
        uni = 1
        cur = nums[0]
        res = 1
        while uni < len(nums):
            if nums[uni] == cur:
                uni+=1
            else:
                nums[i] = nums[uni]
                cur = nums[uni]
                i+=1
                uni+=1
                res+=1
        print(nums)
        return res