# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        if not head:
            return head
        
        left_dummy = ListNode(0)
        right_dummy = ListNode(0)

        left = left_dummy
        right = right_dummy

        current = head
        while(current):
            if current.val<x:
                left.next = current
                left = left.next
            else:
                right.next = current
                right = right.next
            current = current.next
        
        right.next = None
        left.next = right_dummy.next
        return left_dummy.next




