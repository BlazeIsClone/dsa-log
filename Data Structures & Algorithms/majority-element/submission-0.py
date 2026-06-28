class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        data = {}
        count = 0
        key = 0

        for i in range(len(nums)):
            data[nums[i]] = data.get(nums[i], 0) + 1
        
        for k,v in data.items():
            if v > count:
                count = v
                key = k

        return key
