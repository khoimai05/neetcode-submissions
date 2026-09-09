class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k%n
        print(k)
        if k == 0:
            return
        temp1 = nums[-k:]
        temp2 = nums[0:n-k]
        print(temp1) 
        print(temp2)
        nums[0:k] = temp1
        nums[k:] = temp2
        print(nums)

        print(k)