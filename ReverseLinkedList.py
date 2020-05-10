# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def __init__(self):
        self.head = None
        
    def reverseList(self, head):
        linkedItems = list()
        while head:
            linkedItems.append(head.val)
            head = head.next
        linkedItems.reverse()
        
        for item in linkedItems:
            self.createLinks(item)
        
        return self.head
    
    def createLinks(self, item):
        reversedList = ListNode(item)
        if self.head:
            node = self.head
            while node.next:
                node = node.next
            node.next = reversedList
        else:
            self.head = reversedList