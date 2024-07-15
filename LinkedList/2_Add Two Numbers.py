
class Solution(object):
    def removeNthFromEnd(self, head, n):
        current = head
        count = 0
        last_count = 0
        while(current):
            count+=1
            current = current.next
        element = count-n

        if element ==0:
            return head.next

        current = head

        for i in range(element-1):
            current = current.next
        current.next = current.next.next if current.next else None

        return head







        