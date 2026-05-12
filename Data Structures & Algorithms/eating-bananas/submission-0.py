from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        first = 1
        last = max(piles)
        minVal = -1

        while first <= last:
            mid = (first + last) // 2
            tot_time = 0
            for pile in piles:
                # Use ceiling division to compute hours needed for each pile
                tot_time += (pile + mid - 1) // mid

            if tot_time <= h:
                minVal = mid
                last = mid - 1  # Try to find a smaller k
            else:
                first = mid + 1  # k is too small

        return minVal
