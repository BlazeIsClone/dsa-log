class Solution:
    def findMin(self, nums: List[int]) -> int:
        tiny = nums[0]
        for num in nums:
            if num < tiny:
                tiny = num
        return tiny
        