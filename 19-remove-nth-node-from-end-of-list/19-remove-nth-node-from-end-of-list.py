# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head 
        count = 0 
        while (temp):
            count += 1
            temp = temp.next
        current = head
        if( not head or not head.next):
            return None
        fast = head
        for i in range(0,n):
            fast = fast.next
        if not fast:                                            
            return head.next
        for i in range(count-n-1):
            current = current.next
        current.next = current.next.next
        return head