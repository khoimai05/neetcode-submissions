class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i_index, i in enumerate(nums):
            for j_index, j in enumerate(nums):
                if i_index == j_index:
                    continue
                if (i + j == target):
                    print("reacje")
                    return [min(i_index, j_index), max(i_index,j_index)]
