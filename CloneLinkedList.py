class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head is None:
            return None
        
        new_node = {}
        new_head = Node(head.val)
        new_node[head] = new_head

        p1 = head
        p2 = new_head

        while p1.next is not None:
            p2.next = Node(p1.next.val)
            new_node[p1.next] = p2.next
            p2 = p2.next
            p1 = p1.next

        p1 = head
        while p1 is not None:
            if p1.random is not None:
                new_node[p1].random = new_node[p1.random]
            p1 = p1.next

        return new_head