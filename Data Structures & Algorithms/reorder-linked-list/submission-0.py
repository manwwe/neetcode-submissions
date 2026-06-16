# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        curr = slow.next
        slow.next = None

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        first_half = head
        second_half = prev

        while second_half:
            tmp1 = first_half.next
            tmp2 = second_half.next

            first_half.next = second_half
            second_half.next = tmp1

            first_half = tmp1
            second_half = tmp2
        