import enum


class WeightedGapAlign:
    """
    gap_weight = ρ + i * σ
    ρ - gap open penalty
    σ - gap continuation penalty
    i - gap length
    """

    class Flag(enum.Enum):
        main = 0
        lower = 1
        upper = 2

    _main = None
    _upper = None
    _lower = None
    _match_score = 0
    _missmatch_score = 0
    _gap_open = 0
    _gap_cont = 0

    def __init__(self, match_score: int = 1, missmatch_score: int = -1, gap_open: int = 0, gap_cont: int = 0):
        self._match_score = match_score
        self._missmatch_score = missmatch_score
        self._gap_open = gap_open
        self._gap_cont = gap_cont

    def _build_dp(self, s: str, t: str, n: int, m: int):
        self._main[0][0] = 0
        inf = 1e9
        for i in range(n + 1):
            for j in range(m + 1):
                if i == 0:
                    self._upper[i][j] = -inf
                else:
                    self._upper[i][j] = max(
                        self._upper[i - 1][j] + self._gap_cont,
                        self._main[i - 1][j] + self._gap_open + self._gap_cont
                    )
                if j == 0:
                    self._lower[i][j] = -inf
                else:
                    self._lower[i][j] = max(
                        self._lower[i][j - 1] + self._gap_cont,
                        self._main[i][j - 1] + self._gap_open + self._gap_cont
                    )
                if i == 0 and j == 0:
                    continue
                if i == 0:
                    self._main[i][j] = self._lower[i][j]
                    continue
                if j == 0:
                    self._main[i][j] = self._upper[i][j]
                    continue
                self._main[i][j] = max(
                    self._main[i - 1][j - 1] + (self._match_score if s[i - 1] == t[j - 1] else self._missmatch_score),
                    self._upper[i][j],
                    self._lower[i][j]
                )

    def get_max_weight(self):
        if self._main is None:
            raise AssertionError("You need to do align first!")
        return self._main[-1][-1]

    def _build_align(self, s: str, t: str, n: int, m: int) -> tuple[str, str]:
        s1 = ""
        t1 = ""
        flag = self.Flag.main
        i = n
        j = m
        while True:
            if i == 0 and j == 0:
                break
            if i == 0:
                s1 += '-'
                t1 += t[j - 1]
                j -= 1
            elif j == 0:
                t1 += '-'
                s1 += s[i - 1]
                i -= 1
            else:
                if flag == self.Flag.main:
                    if (self._main[i][j] == self._main[i - 1][j - 1] +
                            (self._match_score if s[i - 1] == t[j - 1] else self._missmatch_score)):
                        # match/missmatch
                        s1 += s[i - 1]
                        t1 += t[j - 1]
                        i -= 1
                        j -= 1
                    elif self._main[i][j] == self._upper[i][j]:
                        flag = self.Flag.upper
                    else:
                        flag = self.Flag.lower
                elif flag == self.Flag.upper:
                    if self._upper[i][j] == self._upper[i - 1][j] + self._gap_cont:
                        s1 += s[i - 1]
                        t1 += '-'
                        i -= 1
                    else:
                        s1 += s[i - 1]
                        t1 += '-'
                        i -= 1
                        flag = self.Flag.main
                else:
                    if self._lower[i][j] == self._lower[i][j - 1] + self._gap_cont:
                        s1 += '-'
                        t1 += t[j - 1]
                        j -= 1
                    else:
                        s1 += '-'
                        t1 += t[j - 1]
                        j -= 1
                        flag = self.Flag.main
        return s1[::-1], t1[::-1]

    def align(self, s: str, t: str) -> tuple[str, str]:
        if len(s) > len(t):
            a, b = self.align(t, s)
            return b, a
        # define |s| <= |t|
        n = len(s)
        m = len(t)
        self._main = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
        self._lower = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
        self._upper = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
        self._build_dp(s, t, n, m)
        return self._build_align(s, t, n, m)
