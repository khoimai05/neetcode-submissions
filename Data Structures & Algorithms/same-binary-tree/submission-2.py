class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        dp = deque()
        dq = deque()
        
        # Handle the root pair first
        if p and q and p.val == q.val:
            dp.append(p)
            dq.append(q)
        elif p or q:          # one exists, other doesn't -> mismatch
            return False
        # if both p and q are None, we just fall through with empty deques -> trees are equal (both empty)
        
        while dp:             # loop while there's still work in the queue, not "while q"
            for _ in range(len(dp)):
                pnode = dp.popleft()
                qnode = dq.popleft()
                
                # Check left children
                if pnode.left and qnode.left and pnode.left.val == qnode.left.val:
                    dp.append(pnode.left)
                    dq.append(qnode.left)
                elif pnode.left or qnode.left:
                    return False
                
                # Check right children
                if pnode.right and qnode.right and pnode.right.val == qnode.right.val:
                    dp.append(pnode.right)
                    dq.append(qnode.right)
                elif pnode.right or qnode.right:
                    return False
        return True
        