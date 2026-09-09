class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        my_len = len(s)//2
        for i in range(my_len):
            temp = s[i]
            s[i] = s[-i-1]
            s[-i-1] = temp
        return s