class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        c = 0;
        for i in S:
            if i in J:
                c+=1
                
        return c