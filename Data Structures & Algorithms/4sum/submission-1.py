class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        print(nums)
        n = len(nums)
        res = []
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+2,n):
                l = i + 1
                r = j - 1
                target_sum = target - nums[i] - nums[j]
                while l < r:
                    cur_sum = nums[l] + nums[r]
                    if cur_sum == target_sum:
                        if [nums[i], nums[j],nums[l],nums[r]] not in res:
                            res.append([nums[i], nums[j],nums[l],nums[r]])
                        l+=1
                        while l < r and nums[l-1] == nums[l]:
                            l+=1
                    elif cur_sum < target_sum:
                        l+=1
                    else:
                        r-=1
        return res        

