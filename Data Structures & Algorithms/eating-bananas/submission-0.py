class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles) #O(n) to find max
        res = r

        #O(logm)
        while l<=r:
            k = (l+r) // 2

            totalTime = 0
            for p in piles: #O(n)
                totalTime += math.ceil(p/k) 

            if totalTime <= h:
                res = k
                r = k-1
            else:
                l = k+1
        
        return res
            

