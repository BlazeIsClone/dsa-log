class Solution:
    def reverseString(self, s: List[str]) -> None:
        def rvString(l, r):
            while l < r:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
        rvString(0, len(s) - 1)