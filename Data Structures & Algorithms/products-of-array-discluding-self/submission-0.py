class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        f_list = [] 
        b_list = []
        f_list.append(1)
        cur_prod = 1
        for i in range(1,len(nums)):
            cur_prod*=nums[i - 1]
            f_list.append(cur_prod)
        print(f_list)
        cur_prod = 1
        f_list[len(nums) - 1] *= 1
        for j in range(1,len(nums)):
            cur_prod*= nums[len(nums) - j]
            #print(cur_prod)
            f_list[len(nums) - j - 1]*= cur_prod
        return f_list
            
        