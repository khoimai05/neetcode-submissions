# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        len_check = 0
        cur = head
        while cur!= None:
            len_check +=1
            cur = cur.next
        cur = head
        print(len_check)
        index = len_check - n -1
        if index == -1:
            head = head.next
            return head
        while index != 0:
            cur = cur.next
            print(cur.val)
            index-=1
        if cur.next != None:
            cur.next = cur.next.next
        return head