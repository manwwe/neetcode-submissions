class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for n in num_set:
            if n - 1 not in num_set:
                lenght = 1

                while n + lenght in num_set:
                    lenght += 1

                longest = max(longest, lenght)

        return longest

        