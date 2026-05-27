class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for word in strs:
            sorted_str = "".join(sorted(word))

            if sorted_str not in groups:
                groups[sorted_str] = []
            
            groups[sorted_str].append(word)

        return list(groups.values())
