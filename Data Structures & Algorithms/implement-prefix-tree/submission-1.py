class TrieNode:
    def __init__(self):
        self.array = [None]*26
        self.eow = False
class PrefixTree:
    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            i = ord(c)  - ord('a')
            if cur.array[i] == None:
                cur.array[i] = TrieNode()
            cur = cur.array[i]
        cur.eow = True
    def search(self, word: str) -> bool:
        cur  = self.root
        for c in word:
            i = ord(c)  - ord('a')
            if cur.array[i] == None:
                return False
            else:
                cur = cur.array[i]
        if cur.eow == True:
            return True
        return False
    def startsWith(self, prefix: str) -> bool:
        cur  = self.root
        for c in prefix:
            i = ord(c)  - ord('a')
            if cur.array[i] == None:
                return False
            else:
                cur = cur.array[i]
        return True
        