import operator

class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        res = []
        final = []
        for item in restaurants: 
            if veganFriendly==1:
                if ((item[2] == 1) and (item[3] <= maxPrice) and (item[4] <= maxDistance)):
                    print(item)
                    res.append(item)
            else:
                if((item[3] <= maxPrice) and (item[4] <= maxDistance)):
                    res.append(item)
        
        res = sorted(res, key=operator.itemgetter(1, 0))
        
        for i in res:
            final.append(i[0])
            
        return final
    
                
