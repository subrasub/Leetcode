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
        
        temp = sorted(res, key=lambda k: (k[1], k[0]), reverse=True)
        
        for i in temp:
            final.append(i[0])
            
        return final