# https://leetcode.com/problems/add-two-numbers/
# Tags - Linked List, Math

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode(0)
        current = res
        carry = 0
        
        while(l1 != None or l2 != None):
            first = 0
            second = 0
            sum = 0
            
            if(l1 != None):
                first = l1.val
                l1 = l1.next
                
            if(l2 != None):
                second = l2.val
                l2 = l2.next
            
            sum = first+second+carry
            carry = sum // 10
            current.next = ListNode (sum % 10)
            current = current.next
            
        if carry>0:
            current.next = ListNode(carry)
        
        
        return res.next
