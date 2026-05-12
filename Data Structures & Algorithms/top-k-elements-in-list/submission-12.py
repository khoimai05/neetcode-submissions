class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        e_to_key = {}
        for i in range(len(nums)):
            if nums[i] not in e_to_key:
                e_to_key[nums[i]] = 1
            else:
                e_to_key[nums[i]]+=1
        print(e_to_key)
        bucket = defaultdict(list)
        for key, val in e_to_key.items():
            bucket[val].append(key)
        res = []
        for i in range(len(nums)):
            if k==0:
                break
            print(bucket[len(nums) - i])
            if not bucket[len(nums) - i]:
                continue
            else:
                for j in range(len(bucket[len(nums) - i])):
                    if k==0:
                        break
                    res.append(bucket[len(nums) - i][j])
                    k = k - 1
        return res