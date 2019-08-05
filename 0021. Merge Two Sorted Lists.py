# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy_node=ListNode(0)
        temp_node=dummy_node
        while l1 and l2:
            if l1.val<=l2.val:
                temp_node.next=l1
                l1=l1.next
                temp_node=temp_node.next
            else:
                temp_node.next=l2
                l2=l2.next
                temp_node=temp_node.next
        while l1:
            temp_node.next=l1
            l1=l1.next
            temp_node=temp_node.next
        while l2:
            temp_node.next=l2
            l2=l2.next
            temp_node=temp_node.next
        return dummy_node.next
                
