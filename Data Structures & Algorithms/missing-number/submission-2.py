class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        data = {}
        for i in range(len(nums)):
            data[i] = nums[i]
        for k,v in data.items():
            if k != v:
                return k
        return len(nums)