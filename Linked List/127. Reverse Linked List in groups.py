from sys import setrecursionlimit

setrecursionlimit(10 ** 6)


class Solution:
    def reverseLL(self, head):
        if head is None or head.next is None:
            return head, head
        sh, st = self.reverseLL(head.next)
        st.next = head
        st = st.next
        st.next = None
        return sh, st

    def reverse(self, head, k):
        # Code here
        if head is None:
            return
        st = head
        i = 1
        while i < k and st.next is not None:
            st = st.next
            i += 1
        temp = st.next
        small_head = self.reverse(temp, k)
        st.next = None
        nh, nt = self.reverseLL(head)
        nt.next = small_head
        return nh
