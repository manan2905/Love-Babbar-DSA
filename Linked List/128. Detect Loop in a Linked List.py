class Solution:
    # Function to check if the linked list has a loop.
    def detectLoop(self, head):
        # code here
        if head is None:
            return
        slow, fast = head, head
        while fast is not None and fast.next is not None:
            # we are incrementing them before checking the condition because in the starting they both are head
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            return False
        return True
