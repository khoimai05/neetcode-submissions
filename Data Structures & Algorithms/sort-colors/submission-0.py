class Solution:
    def sortColors(self, nums: List[int]) -> None:
        red = 0
        white = 0
        blue = 0
        length = len(nums)
        for num in nums:
            if num == 0:
                red+=1
            elif num == 1:
                white +=1
            else:
                blue +=1
        for i in range(red):
            nums.append(0)
        for x in range(white):
            nums.append(1)
        for y in range(blue):
            nums.append(2)
        nums[:] = nums[length:]
        return num
