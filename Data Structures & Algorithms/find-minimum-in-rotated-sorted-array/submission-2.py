class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0, len(nums)-1

        if nums[l] < nums[r]: #No rotation
            return nums[l]
        
        #It is rotated, efficiently search
        #O(logn)
        while l<r:
            mid = l+((r-l+1)//2)

            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid
        
        return nums[l]
            