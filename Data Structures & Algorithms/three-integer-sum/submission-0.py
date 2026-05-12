class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        indexes = [i for i in range(0,len(nums))]
        print(indexes)
        lister = []
        seen = set()
        while True:
            for a in range(0,len(nums) - 2):
                for b in range(a+1,len(nums) - 1):
                    for c in range(b+1,len(nums)):
                        if (nums[a] + nums[b] +nums[c] == 0):
                            if tuple(sorted([nums[a] , nums[b], nums[c]])) not in seen:
                                lister.append([nums[a] , nums[b], nums[c]])
                                seen.add(tuple(sorted([nums[a] , nums[b], nums[c]])))
            break
        return lister
