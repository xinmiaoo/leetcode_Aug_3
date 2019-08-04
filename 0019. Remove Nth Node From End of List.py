# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        node1=head
        node2=head
        for i in range(n):
            node2=node2.next
        if node2==None:
            return head.next
        node2=node2.next
        while node2!=None:
            node1=node1.next
            node2=node2.next
        node1.next=node1.next.next
        
        return head
            
