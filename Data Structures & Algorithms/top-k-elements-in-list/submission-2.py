class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}

        for i in range(len(nums)):
            map[nums[i]] = map.get(nums[i], 0) + 1
        
        counts = list(map.keys())

        sorted_items = sorted(map.items(), key=lambda x: x[1])

        result = []
        for k,v in sorted_items[-k:]:
            result.append(k)
        
        return result