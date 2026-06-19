class Solution:
    def encode(self, strs: List[str]) -> str:
        encode_string = ""
        for char in strs:
            len_char = str(len(char)) + "#"
            encode_string += len_char + char

        return encode_string

    def decode(self, s: str) -> List[str]:
        decode_string = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1

            length = int(s[i:j])
            word = s[j + 1 : j + 1 + length]
            decode_string.append(word)

            i = j + 1 + length

        return decode_string
