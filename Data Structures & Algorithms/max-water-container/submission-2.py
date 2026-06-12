class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        container = 0

        while l < r:
            height = min(heights[l], heights[r])
            width = r - l
            area = width * height

            if area > container:
                container = area

            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        
        return container