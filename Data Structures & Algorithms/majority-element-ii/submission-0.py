class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        my_dict = {}
        my_len = len(nums)
        res = []
        for num in nums:
            my_dict[num] = 1+ my_dict.get(num,0)
        for k,v in my_dict.items():
            if v> len(nums)//3:
                res.append(k)
        return res