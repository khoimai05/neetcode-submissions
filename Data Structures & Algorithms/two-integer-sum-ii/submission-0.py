class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        len_str = len(numbers)
        first = 0
        sec = -1
        while (True):
            if (numbers[first] + numbers[sec] == target):
                return [first + 1, len_str + 1 + sec]
            if (numbers[first] + numbers[sec] > target):
                sec = sec - 1
            else:
                first = first + 1
        return [1000000000]