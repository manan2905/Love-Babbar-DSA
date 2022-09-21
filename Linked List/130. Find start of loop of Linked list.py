def detectStart(head):
    slow, fast = head, head
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
        if slow == fast:
            # to remember
            while head != slow:
                head = head.next
                slow = slow.next
            return head
    # if no cycle exists in the linked list
    return None

