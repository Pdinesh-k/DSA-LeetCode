
class Solution(object):
    def createdupList(self,head):
        if not head:
            return head
        
        temp = head

        while temp:
            nextNode = temp.next
            copy = Node(temp.val)
            temp.next = copy
            copy.next = nextNode

            temp = nextNode
    
    def mergedupList(self,head):
        temp = head

        while(temp):
            copyNode = temp.next

            if temp.random:
                copyNode.random = temp.random.next
            else:
                copyNode.random = None

            temp = temp.next.next

    def seperateList(self,head):
        temp = head
        dummyNode = Node(-1)
        dup = dummyNode

        while(temp):
            dup.next = temp.next
            dup = dup.next

            temp.next = temp.next.next
            temp = temp.next
        return dummyNode.next
        


    def copyRandomList(self, head):
        if not head:
            return None

        self.createdupList(head)
        self.mergedupList(head)
        return self.seperateList(head)

        

        


        
        
            

        
        

        