from typing import List
from itertools import chain, cycle


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or len(s) < 2:
            return s
        rows: List[List[str]] = [[] for _ in range(numRows)]
        out: str = ""
        rows_idxs = cycle(chain(range(0, numRows - 1, 1), range(numRows - 1, 0, -1)))
        for char in s:
            rows[next(rows_idxs)].append(char)

        for row in rows:
            out += "".join(row)

        return out
