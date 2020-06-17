# https://leetcode.com/problems/validate-ip-address/
# Tags - String

class Solution:
    def validIPAddress(self, IP: str) -> str:
        if re.search('^((1\d\d|[1-9]\d|\d|25[0-5]|2[0-4]\d)\.){3}(1\d\d|[1-9]\d|\d|25[0-5]|2[0-4]\d)$',IP): 
            return "IPv4"
        elif re.search('^([\da-f]{1,4}:){7}[\da-f]{1,4}$',IP,re.I): 
            return "IPv6"
        else: 
            return "Neither"
