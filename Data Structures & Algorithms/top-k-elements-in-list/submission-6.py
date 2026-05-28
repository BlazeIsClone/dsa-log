class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        fmap = {} 
        buckets = []

        for idx in range(len(nums)):
            fmap[nums[idx]] = fmap.get(nums[idx], 0) + 1

        for _ in range(len(nums) + 1):
            buckets.append([])

        for key, value in fmap.items():
            buckets[value].append(key)
        
        results = []

        for idx in range(len(nums), 0, -1):
            for num in buckets[idx]:
                results.append(num)
                if len(results) == k:
                    return results

        return []