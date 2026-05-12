from typing import List
from collections import defaultdict

class Solution:
    def sort(self, strs: str) -> str:
        return ''.join(sorted(strs))
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)  # Dictionary to store groups of anagrams
        for word in strs:
            sorted_word = self.sort(word)  # Get the sorted version of the word
            anagrams[sorted_word].append(word)  # Group the anagrams
        
        return list(anagrams.values())  # Return the grouped anagrams
