class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapper = defaultdict(list)
        for s in strs:
            sortedS = ''.join(sorted(s))
            mapper[sortedS].append(s)
        
        result = []
        for r in mapper.values():
            result.append(r)
        
        return result
            