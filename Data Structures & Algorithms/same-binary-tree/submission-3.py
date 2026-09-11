class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue = deque()
        queue.append((p, q))
        
        while queue:
            a, b = queue.popleft()
            
            # Validate the pair we just pulled out
            if not a and not b:
                continue          # both None, nothing to compare or enqueue further
            if not a or not b:
                return False      # one exists, the other doesn't
            if a.val != b.val:
                return False      # both exist but values differ
            
            # Only now, after validating, do we queue up the children
            queue.append((a.left, b.left))
            queue.append((a.right, b.right))
        
        return True