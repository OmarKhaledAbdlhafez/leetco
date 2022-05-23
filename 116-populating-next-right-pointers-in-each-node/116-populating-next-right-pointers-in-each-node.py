"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def point (self , node1 , node2):
        if not node1 and not node2 :
            return
        node1.next = node2
        self.point(node1.left , node1.right)
        self.point(node2.left , node2.right)
        self.point(node1.right , node2.left)
        
        
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root :
            return None 
        self.point(root.left, root.right)
        return root
        
        