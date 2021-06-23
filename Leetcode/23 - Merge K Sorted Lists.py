from queue import PriorityQueue
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        head = temp = ListNode(0)

        priority = PriorityQueue(maxsize=len(lists))

        for index, lis in enumerate(lists):
            if lis:
                priority.put((lis.val, index, lis))

        while priority.qsize()>0:
            item = priority.get()

            temp.next, idx = item[2], item[1]
            temp = temp.next

            if temp.next:
                priority.put((temp.next.val, idx, temp.next))

        return head.next
