# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverse_inside(self,curr,k):
        prev = None
        tail = curr
        count = 0
        for i in range(k):
            if not curr:
                return prev
            nextt = curr.next
            curr.next = prev
            prev = curr
            curr = nextt
            count+=1
        tail.next = curr
        return prev

    def reverseKGroup(self, head, k):
        curr = head
        count = 0

        while curr and count<k:
            curr = curr.next
            count+=1
        if count<k:
            return head

        new_head = self.reverse_inside(head,k)
        head.next = self.reverseKGroup(curr,k)
        return new_head



            



        
        