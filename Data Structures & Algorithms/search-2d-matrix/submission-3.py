class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        acLen = len(matrix) * len(matrix[0])
        print(acLen)
        l = 0
        r = acLen - 1
        while l <= r:
            print(r,l)
            mid = (r + l) // 2
            i = mid // len(matrix[0])
            j = mid - i*len(matrix[0])
            if matrix[i][j] < target:
                l+=1
            elif matrix[i][j] > target:
                r-=1
            else:
                return  True 
        return False

        