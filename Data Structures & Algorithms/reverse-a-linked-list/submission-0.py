# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        if head.next == None:
            return head
        one = head
        two = one.next
        one.next = None
        three = two.next
        while three != None:
            print(one.val , two.val, three.val)
            two.next = one
            one = two
            two = three
            three = three.next
        two.next = one  # Reverse the last connection

        return two        
        