class Solution:
  def maxNumberOfBalloons(self, text: str) -> int:
    table = {"b": 0, "a": 0, "l": 0, "o": 0, "n": 0}

    for i in text:
      if i in table:
        table[i] += 1

    table["l"] //= 2
    table["o"] //= 2

    return min(table.values())