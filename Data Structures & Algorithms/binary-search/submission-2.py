class Solution:
    def search(self, nums, target: int) -> int:
        l, r = 0, len(nums)

        while l<r:
            m = l + ((r-l) // 2)
            if nums[m] > target:
                r=m
            
            elif nums[m] == target:
                return m
                
            else:
                l=m+1

        return  -1