# https://leetcode.com/problems/robot-bounded-in-circle/
class Solution:
  def isRobotBounded(self, instructions: str) -> bool:
    x = y = 0
    directions = [[0,1], [1, 0], [0, -1], [-1, 0]]
    idx = 0
    for i in instructions:
      if i=='R':
        idx = (idx + 1) % 4
      elif i=='L':
        # one turn to left = three turns to right
        idx = (idx + 3) % 4
      else:
        x += directions[idx][0]
        y += directions[idx][1]

    return (x==0 and y==0) or idx!=0