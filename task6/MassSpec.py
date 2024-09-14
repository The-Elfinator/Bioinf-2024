alphabet = ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y']
masses =   [71 , 103, 115, 129, 147,  57, 137, 113, 128, 113, 131, 114,  97, 128,  156, 87, 101,  99, 186, 163]


def get_mass(acid):
    ind = alphabet.index(acid)
    return masses[ind]


def ideal_spectrum(s):
    n = len(s)
    spec = {0}
    mass_pref = [0 for _ in range(n)]
    mass_pref[0] = get_mass(s[0])
    for i in range(1, n):
        mass_pref[i] = mass_pref[i - 1] + get_mass(s[i])
    mass_suff = [0 for _ in range(n)]
    mass_suff[-1] = get_mass(s[-1])
    for i in range(n - 2, -1, -1):
        mass_suff[i] = mass_suff[i + 1] + get_mass(s[i])
    for m in mass_pref:
        spec.add(m)
    for m in mass_suff:
        spec.add(m)
    ideal_spec = sorted(spec)
    return ideal_spec


def find_peptide(spectrum, g):
    paths = []

    def sets_are_equal(a, b):
        if len(a) != len(b):
            return False
        for i in range(len(a)):
            if a[i] != b[i]:
                return False
        return True

    def dfs(v, cur_path):
        if v == len(g) - 1:
            peptide = cur_path
            if sets_are_equal(list(ideal_spectrum(peptide)), spectrum):
                return peptide
            return None
        for to, acid in g[v]:
            new_path = cur_path + acid
            paths.append(new_path)
            out = dfs(to, new_path)
            if out is not None:
                return out

    return dfs(0, '')


def reconstruct(spectrum):
    n = len(spectrum)
    g = [[] for _ in range(n)]
    for i in range(n-1):
        for j in range(i+1, n):
            delta = spectrum[j] - spectrum[i]
            try:
                ind = masses.index(delta)
            except ValueError:
                continue
            acid = alphabet[ind]
            g[i].append((j, acid))
    # for i in range(n):
    #     print(i, g[i])
    return find_peptide(spectrum, g)


spec = list(map(int, input().split()))
pep = reconstruct(spec)
print(pep)
