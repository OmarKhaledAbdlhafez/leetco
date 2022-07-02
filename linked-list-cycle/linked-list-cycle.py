# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        
        visted = []
        curr = head.next
        
        while (curr):
            if curr in visted :
                return True
            visted.append(curr)
            curr = curr.next
        
        return False 