class Solution:
    def isValid(self, s: str) -> bool:
        dicter = {
            '(' : ')',
            '{' : '}',
            '[' : ']' 
        }
        store = []
        for i in s:
            if i in dicter:
                store.append(dicter[i])
                continue
            else:
                if len(store) == 0:
                    return False
                if store[len(store) - 1] == i:
                    store.pop()
                else:
                    return False
        if len(store) != 0:
            return False
        return True
        
        