# https://leetcode.com/problems/subdomain-visit-count/
# Tags - Hash Map

from collections import Counter

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        table = Counter()
        for domain in cpdomains:
            count, dom = domain.split(' ')
            count = int(count)
            fragments = dom.split('.')
            
            for i in range(len(fragments)):
                table['.'.join(fragments[i:])] += count
        
        return ["{} {}".format(count, domain) for domain, count in table.items()]
