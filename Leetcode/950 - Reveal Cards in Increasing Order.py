# https://leetcode.com/problems/reveal-cards-in-increasing-order/
# Tags - Array

import queue
class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        if(len(deck)==0):
            return -1;
        if(len(deck)==1):
            return deck
        # Sort the given array
        deck.sort()
        
        # Initialize the res list
        n = len(deck)
        res = [None]*n
        
        dq = collections.deque(range(n))
        # print(dq.popleft(), dq.pop())
            
        for i in range(n):
            index = dq.popleft()
            res[index] = deck[i]
            if(dq):
                dq.append(dq.popleft())
            
        return res