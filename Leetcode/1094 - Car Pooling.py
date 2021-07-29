class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        temp = [0]*1001

        for trip in trips:
            temp[trip[1]] += trip[0]
            temp[trip[2]] -= trip[0]

        people = 0
        for val in temp:
            people += val
            if people > capacity:
                return False

        return True