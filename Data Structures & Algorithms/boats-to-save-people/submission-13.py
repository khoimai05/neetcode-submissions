class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # 1. Sort the people by their weight
        people.sort()
        
        l, r = 0, len(people) - 1
        boats = 0
        
        # 2. Pair people from both ends
        while l <= r:
            # If the heaviest and lightest person can share a boat
            if people[l] + people[r] <= limit:
                l += 1  # The light person gets a seat
            
            # The heaviest person always gets a boat
            r -= 1
            boats += 1
            
        return boats