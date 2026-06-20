class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        lowest = nums[0]

        while l < r:
            if nums[l] < nums[r]:
                lowest = min(nums[l], lowest)
                r -= 1
            else:
                lowest = min(nums[r], lowest)
                l += 1
        
        return lowest

        