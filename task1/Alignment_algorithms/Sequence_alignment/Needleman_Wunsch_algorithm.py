class NeedlemanWunschAlgorithm:
    _M = 0
    _X = 0
    _G = 0
    _dp = None
    _matrix = None

    def __init__(self, match_score: int = 1, missmatch_score: int = -1, gap_score: int = -2, matrix=None):
        self._M = match_score
        self._X = missmatch_score
        self._G = gap_score
        self._matrix = matrix

    def _rule(self, s, t, i, j):
        if self._matrix is None:
            return self._M if s[i - 1] == t[j - 1] else self._X
        else:
            get_ind = {
                'A': 0,
                'C': 1,
                'D': 2,
                'E': 3,
                'F': 4,
                'G': 5,
                'H': 6,
                'I': 7,
                'K': 8,
                'L': 9,
                'M': 10,
                'N': 11,
                'P': 12,
                'Q': 13,
                'R': 14,
                'S': 15,
                'T': 16,
                'V': 17,
                'W': 18,
                'Y': 19
            }
            ind_s = get_ind[s[i - 1]]
            ind_t = get_ind[t[j - 1]]
            return self._matrix[ind_s][ind_t]

    def _build_dp(self, s: str, t: str, n: int, m: int) -> None:
        self._dp[0][0] = 0
        for j in range(m + 1):
            self._dp[0][j] = self._G * j
        for i in range(n + 1):
            self._dp[i][0] = self._G * i
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                self._dp[i][j] = max(
                    self._dp[i - 1][j - 1] + self._rule(s, t, i, j),
                    self._dp[i][j - 1] + self._G,
                    self._dp[i - 1][j] + self._G
                )

    def _build_align(self, s: str, t: str, n: int, m: int) -> tuple[str, str]:
        s1 = ""
        t1 = ""
        i = n
        j = m
        while True:
            if i == 0 and j == 0:
                break
            elif i == 0:
                s1 += '-'
                t1 += t[j - 1]
                j -= 1
            elif j == 0:
                s1 += s[i - 1]
                t1 += '-'
                i -= 1
            else:
                if self._dp[i][j] == self._dp[i - 1][j - 1] + self._rule(s, t, i, j):
                    # match or missmatch
                    s1 += s[i - 1]
                    t1 += t[j - 1]
                    i -= 1
                    j -= 1
                elif self._dp[i][j] == self._dp[i][j - 1] + self._G:
                    s1 += '-'
                    t1 += t[j - 1]
                    j -= 1
                else:
                    s1 += s[i - 1]
                    t1 += '-'
                    i -= 1
        return s1[::-1], t1[::-1]

    def align(self, s: str, t: str) -> tuple[str, str]:
        if len(s) > len(t):
            b, a = self.align(t, s)
            return a, b
        # define: |s| <= |t|
        n = len(s)
        m = len(t)
        self._dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
        self._build_dp(s, t, n, m)
        return self._build_align(s, t, n, m)
