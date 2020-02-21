# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head==None or head.next==None:
            return None
        
        slow = fast = res = head
        
        while (fast and fast.next):
            if (fast==None or fast.next==None):
                return None
            
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                while(slow != res):
                    slow = slow.next
                    res = res.next
                return slow
        return None
    
