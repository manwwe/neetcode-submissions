class Solution:
    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        decode_str = []
        i = 0
        n = len(s)

        while i < n:
            j = s.find("#", i)

            if j == -1:
                break

            length = int(s[i:j])
            word = s[j + 1 : j + 1 + length]
            decode_str.append(word)

            i = j + 1 + length

        return decode_str
