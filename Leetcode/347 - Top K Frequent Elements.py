# https://leetcode.com/problems/top-k-frequent-elements/
# Tags - Hash Table, Heap

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        return heapq.nlargest(k, count.keys(), key = count.get)