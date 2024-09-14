from math import ceil


class OptimizedAlignment:
    _M = 0
    _X = 0
    _G = 0
    _dp = None

    def __init__(self, match_score: int = 1, missmatch_score: int = -1, gap_score: int = -2):
        self._M = match_score
        self._X = missmatch_score
        self._G = gap_score

    def _build_dp(self, left: int = 0, right: int = 0):
        mid = ceil((right - left) / 2)

    def _mem_align(self, s: str, t: str) -> tuple[str, str]:
        n = len(s)
        m = len(t)
        if n <= 10:
            self._dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
            self._build_dp(right=n)  # TODO: implement me
        # TODO: todo todo todo aaaaaaaaaaaa
        return "", ""

    def align(self, s: str, t: str) -> tuple[str, str]:
        if len(s) > len(t):
            b, a = self.align(t, s)
            return a, b
        # define: |s| <= |t|
        return self._mem_align(s, t)
