class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        for c in strs:
            result.setdefault("".join(sorted(c)), []).append(c)

        return list(result.values())
        