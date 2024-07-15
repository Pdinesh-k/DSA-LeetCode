# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        if not head or not head.next:
            return head

        new_head = head.next       
        current = head
        prev = None
        while(current and current.next):
            first = current
            second = current.next

            first.next = second.next
            second.next = first
            if prev:
                prev.next = second
            prev = first
            current = first.next
        return new_head
        