# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head # Initialise temp
        count = 0 # Initialise count
 
        # Loop while end of linked list is not reached
        while (temp):
            count += 1
            temp = temp.next
        m=0
        if count % 2 ==0 :
            m = int(count /2) +1
        else :
            m = int(count /2) +1
        if not head :
            return None 
        if not head.next :
            return head
        current = head
        for i in range(m-1):
            current = current.next
        
        return current
        