from collections import deque

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # Step 1: Load all nodes into deque
        dq = deque()
        cur = head
        while cur:
            dq.append(cur)
            cur = cur.next

        # Step 2: Reorder using deque
        dummy = ListNode(0)
        cur = dummy
        toggle = True  # alternate between left and right

        while dq:
            if toggle:
                cur.next = dq.popleft()
            else:
                cur.next = dq.pop()
            cur = cur.next
            toggle = not toggle

        # Terminate the list
        cur.next = None
