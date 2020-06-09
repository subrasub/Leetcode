# https://leetcode.com/problems/palindrome-linked-list/
# Tags - Linked Lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True
        
        res = []
        
        while head:
            res.append(head.val)
            head = head.next
        
        return res[::-1]==res
