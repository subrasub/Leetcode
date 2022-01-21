class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        def binarySearch(row):
            start, end = 0, len(mat[0])

            while start<end:
                mid = start + (end-start)//2

                if row[mid] == 1:
                    start = mid + 1
                else:
                    end = mid

            return start

        q = []

        for i, row in enumerate(mat):
            strength = binarySearch(row)
            entry = (-strength, -i)

            if len(q)<k or entry > q[0]:
                heapq.heappush(q, entry)
            if len(q)>k:
                heapq.heappop(q)


        res = []

        while q:
            strength, i = heapq.heappop(q)
            res.append(-i)

        res = res[::-1]
        return res
