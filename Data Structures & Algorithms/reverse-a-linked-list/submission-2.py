class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # The previous node starts as None because the original head
        # will become the final tail of the reversed list.
        previous = None

        # Start at the original head and process each node once.
        current = head

        # Continue until every node has had its pointer reversed.
        while current is not None:
            # Save the next node before changing current.next,
            # otherwise we would lose access to the remaining list.
            next_node = current.next

            # Reverse the current node's pointer so it points backward.
            current.next = previous

            # Move previous forward; it is now the front of the reversed portion.
            previous = current

            # Move current forward using the saved node.
            current = next_node

        # When current is None, previous is the new head of the reversed list.
        return previous
