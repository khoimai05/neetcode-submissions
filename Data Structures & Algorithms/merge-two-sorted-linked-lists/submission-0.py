# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur_1 = list1
        cur_2 = list2   
        # Handle edge cases
        if cur_1 is None:
            return cur_2
        if cur_2 is None:
            return cur_1

        head = None
        if cur_1.val < cur_2.val:
            head = cur_1
            cur_1 = cur_1.next
        else:
            head = cur_2
            cur_2 = cur_2.next
        prev = head
        while True:
            if cur_1 != None and cur_2 != None:
                if cur_1.val < cur_2.val:
                    prev.next = cur_1
                    prev = prev.next
                    cur_1 = cur_1.next
                else:
                    prev.next = cur_2
                    prev = prev.next
                    cur_2 = cur_2.next
            elif cur_1 == None and cur_2 == None:
                break
            elif cur_1 == None:
                prev.next = cur_2
                break
            elif cur_2 == None:
                prev.next = cur_1
                break
        return head