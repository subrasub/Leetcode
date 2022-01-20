# https://leetcode.com/problems/top-k-frequent-elements/
# Tags - Hash Table, Heap

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        return heapq.nlargest(k, count.keys(), key = count.get)

    def topKFrequent2(self, nums: List[int], k: int) -> List[int]:
        res = []

        count = Counter(nums)

        max_heap = [(-val, key) for key, val in count.items()]

        heapq.heapify(max_heap)

        for _ in range(k):
            res.append(heapq.heappop(max_heap)[1])

        return res