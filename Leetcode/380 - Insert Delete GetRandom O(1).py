# https://leetcode.com/problems/insert-delete-getrandom-o1/
# Tags - Array, Hash Table, Design

class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.res = []
        self.table = {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.table:
            self.res.append(val)
            self.table[val] = len(self.res) - 1
            return True
        return False
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.table:
            index = self.table[val]
            last = self.res[-1]
            self.res[index] = last
            self.table[last] = index
            self.res.pop()
            del self.table[val]
            return True
        return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.res)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
