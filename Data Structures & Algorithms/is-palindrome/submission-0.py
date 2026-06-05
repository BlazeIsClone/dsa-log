class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = "".join(filter(str.isalnum, s)).lower()
        left, right = 0, len(word) - 1

        while (left < right):
            if word[left] != word[right]:
                return False
            else:
                left += 1
                right -= 1
        
        return True