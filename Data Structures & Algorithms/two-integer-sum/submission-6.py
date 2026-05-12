class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dicter = {}
        for index, num in enumerate(nums):
            dicter[num] = index 
        for index, num in enumerate(nums):
            check = target - num
            if check in dicter and dicter[check] != index:
                return [index,dicter[check]]
        return []