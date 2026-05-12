class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Remove non-alphanumeric characters and convert to lowercase
        s = ''.join(char.lower() for char in s if char.isalnum())
        for i in range(len(s) // 2):
            if s[i] != s[len(s) - 1 -i]:
                return False
        return True
