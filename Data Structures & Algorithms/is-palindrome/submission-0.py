class Solution:
    def isPalindrome(self, s: str) -> bool:
        alpha = []
        for char in s:
            if char.isalnum():
                alpha.append(char.lower())

        left = 0
        right = len(alpha) - 1

        while left < right:
            if alpha[left] != alpha[right]:
                return False
            else:
                left += 1
                right -= 1

        return True
        