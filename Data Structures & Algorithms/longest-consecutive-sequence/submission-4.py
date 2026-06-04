class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        current = 1
        best = 1

        if nums == []:
            return 0

        for i in range(len(nums)):
            if nums[i] == nums[i-1] + 1:
                current += 1
                print(best)
                best = max(best, current)
            elif nums[i] == nums[i-1]:
                continue
            else:
                current = 1
        
        return best
