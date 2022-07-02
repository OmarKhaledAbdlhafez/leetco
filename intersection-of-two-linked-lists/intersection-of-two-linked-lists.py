# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        nodes = set()
        curra = headA
        currb = headB
        
        while(curra):
            nodes.add(curra)
            curra = curra.next
            
        while (currb):
            if currb in nodes :
                return currb
            currb = currb.next
        
        return None