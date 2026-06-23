class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        char_set = set()
        left = 0
        max_legth = 0

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1

            char_set.add(s[right])

            max_legth = max(max_legth, right - left + 1)

        return max_legth

        