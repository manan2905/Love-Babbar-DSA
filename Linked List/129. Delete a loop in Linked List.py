class Solution:
    # Function to remove a loop in the linked list.
    def removeLoop(self, head):
        ps = None
        curr = head
        slow, fast = head, head
        while fast is not None and fast.next is not None:
            ps = slow
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                while curr != slow:
                    curr = curr.next
                    ps = slow
                    slow = slow.next
                ps.next = None
                break
        return head
