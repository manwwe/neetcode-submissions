class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            # Skip non-alphanumeric characters from the left
            while left < right and not s[left].isalnum():
                left += 1
            
            # Skip non-alphanumeric characters from the right
            while left < right and not s[right].isalnum():
                right -= 1

            # Get ASCII values
            char_l = ord(s[left])
            char_r = ord(s[right])

            # Convert uppercase to lowercase using ASCII values (add 32)
            if 65 <= char_l <= 90:
                char_l += 32
            if 65 <= char_r <= 90:
                char_r += 32

            # Compare the ASCII values
            if char_l != char_r:
                return False
            
            left += 1
            right -= 1

        return True