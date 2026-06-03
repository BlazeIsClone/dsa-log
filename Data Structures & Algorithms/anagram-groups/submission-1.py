class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for str in strs:
            count = [0] * 26
            for char in str:
                count[ord(char) - ord('a')] += 1
            if tuple(count) not in res:
                res[tuple(count)] = []
            res[tuple(count)].append(str)
        return list(res.values())
