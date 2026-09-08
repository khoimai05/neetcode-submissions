class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        my_set = set(nums)
        looked = set()
        longest = 1
        res=0
        for items in my_set:
            longest = 1
            if items in looked:
                continue
            else:
                cur = items
                while cur - 1 not in looked and cur -1 in my_set:
                    longest += 1
                    looked.add(cur-1)
                    cur = cur -1
                cur = items 
                while cur + 1 not in looked and cur+1 in my_set:
                    longest+=1
                    looked.add(cur+1)
                    cur = cur + 1
            res = max(longest,res)
        return res