# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        
        dummy_node=ListNode(0)
        dummy_node.next=head
        temp=dummy_node
        node1=head
        node2=head.next
        while 1:
            temp.next=node1.next
            node1.next=node2.next
            node2.next=node1
            temp=node1
            node1=node1.next
            if not node1:
                break
            node2=node1.next
            if not node2:
                break

        return dummy_node.next
