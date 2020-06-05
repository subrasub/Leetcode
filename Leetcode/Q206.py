# https://leetcode.com/problems/reverse-linked-list/
# Tags - Linked Lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Recursive approach
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        temp = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        
        return temp
    
    # Iterative approach
    def reverseList(self, head: ListNode) -> ListNode:
        current = head
        prev = None
        
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        
        return prev
