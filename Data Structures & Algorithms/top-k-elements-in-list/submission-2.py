class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range(len(nums) + 1)]
        count = Counter(nums)
        result = []

        for i, v in count.items():
            buckets[v].append(i)

        for bucket in reversed(buckets):
            for num in bucket:
                result.append(num)

                if len(result) == k:
                    return result
        