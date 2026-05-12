# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        head1 = l1
        head2 = l2
        past_l1 = None 
        past_l2 = None
        while l1 and l2:
            val = l1.val + l2.val + carry
            if val >= 10:
                l1.val = val%10
                carry = 1
            else:
                l1.val = val
                carry = 0
            past_l1 = l1
            past_l2 = l2
            l1 = l1.next
            l2 = l2.next
        if l2:
            past_l1.next = l2
        cur = past_l1
        if carry != 1:
            return head1
        while carry == 1:
            if cur.next == None:
                cur.next = ListNode(1)
                carry = 0
            else:
                cur = cur.next
                val = cur.val + 1
                if val >=10:
                    cur.val = val%10
                    continue
                else:
                    cur.val = val
                    carry = 0
        return head1
                
                

    

            
        

