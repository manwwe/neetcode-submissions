class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for index, value in enumerate(nums):
            current_sum = target - value
            if value in seen:
                return [seen[value], index]
            seen[current_sum] = index
        return []
        