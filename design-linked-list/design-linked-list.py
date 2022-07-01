class Node:
    def __init__(self, val=0, nxt=None):
        self.val = val
        self.next = nxt

class MyLinkedList(object):

    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index):
        if index < 0 or index >= self.size:
            return -1
        if not self.head:
            return -1
        t = self.head
        for i in range(index):
            t = t.next
        return t.val

    def addAtHead(self, val):
        node = Node(val)
        node.next = self.head
        self.head = node
        self.size += 1

    def addAtTail(self, val):
        self.size += 1
        t = self.head
        if not self.head:
            self.head = Node(val)
            return
        while t.next:
            t = t.next
        t.next = Node(val)

    def addAtIndex(self, index, val):
        if index < 0 or index > self.size:
            return
        self.size += 1
        if index == 0:
            self.addAtHead(val)
        elif index == self.size:
            self.addAtTail(val)
        else:
            t = self.head
            for i in range(index-1):
                t = t.next
            node = Node(val)
            node.next = t.next
            t.next = node

    def deleteAtIndex(self, index):
        if index < 0 or index >= self.size:
            return
        t = self.head
        if index == 0:
            self.head = t.next
        else:
            for i in range(index-1):
                t = t.next
            t.next = t.next.next
        self.size -= 1 