class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for index, value in enumerate(nums):
            diff = target - value
            if value in seen:
                return [seen[value], index]
            seen[diff] = index
        return []
        