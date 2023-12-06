class Solution:
    def reverse(self, x: int) -> int:
        out = int(str(x)[::-1]) if x >= 0 else -int((str(x)[1:])[::-1])
        return out if abs(out) < (2**31) else 0
