# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        node = head
        max_val = -1001
        while node is not None:
            print(node.val)
            if max_val < node.val:
                max_val = node.val
                node = node.next  
            else:
                return True
        return False     