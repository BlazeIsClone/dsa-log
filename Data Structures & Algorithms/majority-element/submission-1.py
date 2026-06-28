class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        data, res = {}, {"k": 0, "v": 0}

        for i in range(len(nums)):
            data[nums[i]] = data.get(nums[i], 0) + 1
        
        for k,v in data.items():
            if v > res["v"]:
                res["k"], res["v"] = k, v

        return res["k"]
