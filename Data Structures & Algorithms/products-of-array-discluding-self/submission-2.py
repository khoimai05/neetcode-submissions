class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        forward = []*len(nums)
        backward = []*len(nums)
        f_sum = 1
        b_sum = 1
        for i in range(len(nums)):
            if i == 0:
                f_sum =  1
            else:
                f_sum = f_sum*nums[i-1]
            forward.append(f_sum)
        for j in range(len(nums)):
            if j == 0:
                b_sum =  1
            else:
                print(b_sum)
                b_sum = b_sum*nums[len(nums)- j]
            backward.append(b_sum)
        res = []
        for i in range(len(nums)):
            res.append(forward[i] * backward[-i-1])
        return res
        