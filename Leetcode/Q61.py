# https://leetcode.com/problems/rotate-list/
# Tags - Linked list, Two Pointers

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if (not head) or (not head.next) or (k==0):
            return head
        
        ref = head
        # n is the length of the Linked List
        n = 1
        
        while(ref.next):
            n += 1
            ref = ref.next
        
        rotations = k%n
        
        if rotations==0:
            return head
        
        fast = slow = head
        
        for i in range(rotations):
            fast = fast.next
        
        while fast.next:
            slow = slow.next
            fast = fast.next
        
        temp = slow.next
        fast.next = head
        slow.next = None
        head = temp
        
        return head
