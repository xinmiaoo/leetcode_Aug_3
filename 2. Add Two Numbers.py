# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1==None:
            return l2
        if l2==None:
            return l1
        dummy_node=ListNode(0)
        ans=0
        b=0
        node_l1=l1
        node_l2=l2
        node_l3=dummy_node
        while node_l1!=None and node_l2!=None:
            sum_two=node_l1.val+node_l2.val+b
            if sum_two<10:
                node_l3.next=ListNode(sum_two)
                b=0
            else:
                node_l3.next=ListNode(sum_two-10)
                b=1
            node_l3=node_l3.next
            node_l1=node_l1.next
            node_l2=node_l2.next

        while node_l1!=None:
            if node_l1.val+b<10:
                node_l3.next=ListNode(node_l1.val+b)
                b=0
            else:
                node_l3.next=ListNode(0)   
                b=1
            node_l3=node_l3.next            
            node_l1=node_l1.next
        while node_l2!=None:
            if node_l2.val+b<10:
                node_l3.next=ListNode(node_l2.val+b)
                b=0
            else:
                node_l3.next=ListNode(0)  
                b=1
            node_l3=node_l3.next            
            node_l2=node_l2.next
        if b==1:
            node_l3.next=ListNode(1)
        
        return dummy_node.next
                
