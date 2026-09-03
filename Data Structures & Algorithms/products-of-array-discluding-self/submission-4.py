class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        pre,post = [0]*l,[0]*l
        re,ost = 1,1
        for i in range(l):
            if i == 0:
                pre[i] = 1
                post[-i-1] = 1
            else:
                pre[i] = re
                post[-1-i] = ost
            re*=nums[i]
            ost*=nums[-i-1]
        res = []
        for i in range(l):
            res.append(pre[i]*post[i])
        return res