from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dicter = defaultdict(list)
        for val in strs:
            key = "".join(sorted(val))
            dicter[key].append(val)
        res = []
        for value in dicter.values():
            res.append(value)
        return res