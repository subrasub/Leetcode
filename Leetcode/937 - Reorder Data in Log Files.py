# https://leetcode.com/problems/reorder-data-in-log-files/

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter = []
        digits = []
        
        for i in range(len(logs)):
            target = (logs[i].split(' '))[1]
            if  target.isnumeric():
                digits.append(logs[i])
            else:
                letter.append(logs[i])
        
        letter.sort(key = lambda x: x.split()[1])
        letter.sort(key = lambda x: x.split()[1:])
        
        return letter+digits