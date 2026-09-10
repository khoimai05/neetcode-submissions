class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        n = len(asteroids)
        i = 0  # Initialize the index pointer
        
        while i < n:
            curr = asteroids[i]  # Get the current asteroid
            
            # Case 1: Moving right (> 0) never causes an immediate collision
            if curr > 0:
                stack.append(curr)
                i += 1  # Safe to move to the next asteroid
                
            # Case 2: Moving left (<= 0) might collide with a right-moving asteroid in the stack
            else:
                if stack and stack[-1] > 0:
                    # If the stack top is bigger, the current asteroid is destroyed
                    if abs(stack[-1]) > abs(curr):
                        i += 1  # Current asteroid is gone, move to the next one
                        
                    # If they are equal size, both are destroyed
                    elif abs(stack[-1]) == abs(curr):
                        stack.pop()
                        i += 1  # Both gone, move to the next one
                        
                    # If the current asteroid is bigger, it destroys the stack top
                    else:
                        stack.pop()

                else:
                    # No right-moving asteroid to collide with, safe to add
                    stack.append(curr)
                    i += 1  # Move to the next asteroid
                    
        return stack