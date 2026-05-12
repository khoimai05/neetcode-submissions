class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Remove non-alphanumeric characters and convert to lowercase
        s = ''.join(char.lower() for char in s if char.isalnum())
        
        # Use the length of the string
        str_len = len(s)
        
        # Check for palindrome
        for i in range(str_len // 2):
            if s[i] != s[-i - 1]:
                return False
        return True
