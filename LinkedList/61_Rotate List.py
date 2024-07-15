# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        if not head or not head.next or k==0:
            return head
        current = head
        nodes = 1

        while(current.next):
            current = current.next
            nodes+=1

        k = k%nodes
        if k==0:
            return head

        current.next = head
        steps_to_new_node = nodes-k
        new_tail = head
        
        for i in range(steps_to_new_node-1):
            new_tail = new_tail.next
        new_head = new_tail.next
        new_tail.next = None
        return new_head
            
            

            
        