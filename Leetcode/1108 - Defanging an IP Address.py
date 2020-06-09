# https://leetcode.com/problems/defanging-an-ip-address/
# Tags - String

class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace(".","[.]")