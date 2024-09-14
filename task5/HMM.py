s = input()
# 0 is for P
# 1 is for N
A = [[0.9, 0.1],
     [0.2, 0.8]]
B = [{'C': 0.4, 'G': 0.4, 'T': 0.1, 'A': 0.1},
     {'C': 0.2, 'G': 0.2, 'T': 0.3, 'A': 0.3}]
P = [0.5, 0.5]
T = len(s)
O = ' ' + s
sigma = [[0] * (T + 1) for _ in range(2)]
for j in range(2):
    sigma[j][1] = P[j] * B[j][O[1]]
for t in range(2, T + 1):
    for j in range(2):
        sigma[j][t] = max(sigma[0][t - 1] * A[0][j] * B[j][O[t]], sigma[1][t - 1] * A[1][j] * B[j][O[t]])
for i in range(2):
    print(sigma[i])
#TODO: find answer using sigma
phi = [['-'] * (T+1) for _ in range(2)]
for t in range(1, T):
    for j in range(2):
        phi[j][t+1] = 'P' if sigma[0][t] * A[0][j] * B[j][O[t+1]] > sigma[1][t] * A[1][j] * B[j][O[t+1]] else 'N'
for i in range(2):
    print(phi[i])

S_cap = ['-' for _ in range(T+1)]
S_cap[T] = 'P' if sigma[0][T] > sigma[1][T] else 'N'
for t in range(T-1, 0, -1):
    ind = 0 if S_cap[t+1] == 'P' else 1
    S_cap[t] = phi[ind][t+1]
print(S_cap)
print(''.join(S_cap[1:]))
