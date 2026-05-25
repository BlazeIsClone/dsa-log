class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        list1 = sorted(list(s))
        list2 = sorted(list(t))

        if len(list1) != len(list2):
            return False;

        if list1 == list2:
            return True

        return False