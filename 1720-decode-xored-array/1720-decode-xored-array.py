class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        decode = [first]
        for i in range(len(encoded)):
            decode.append(decode[i] ^ encoded[i])
        return decode
        