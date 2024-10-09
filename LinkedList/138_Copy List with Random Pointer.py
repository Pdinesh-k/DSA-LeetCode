# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        if not head or not head.next:
            return head

        temp = head
        nodes = 0

        while(temp):
            nodes+=1
            temp=temp.next
        
        k = k%nodes

        if k<=0:
            return head

        reach = nodes-k

        curr = head

        for i in range(reach):
            if i!=reach-1:
                curr = curr.next
        
        next_node = curr.next
        curr.next = None
        next_node1 = next_node

        while(next_node.next):
            next_node = next_node.next
        next_node.next = head
        return next_node1


            
        
        



            
            

            
        