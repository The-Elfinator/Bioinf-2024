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
alpha = [[0] * (T+1) for _ in range(2)]
beta = [[0] * (T+1) for _ in range(2)]
for j in range(2):
    alpha[j][1] = P[j] * B[j][O[1]]
for t in range(2, T+1):
    for j in range(2):
        for i in range(2):
            alpha[j][t] += alpha[i][t-1] * A[i][j] * B[j][O[t]]
# for i in range(2):
#     print(alpha[i])

beta[0][T] = 1
beta[1][T] = 1
for j in range(2):
    beta[j][T-1] = B[0][O[T]] * A[j][0] + B[1][O[T]] * A[j][1]
for t in range(T-2, 0, -1):
    for j in range(2):
        for i in range(2):
            beta[j][t] += beta[i][t+1] * B[i][O[t+1]] * A[j][i]
# for i in range(2):
#     print(beta[i])

rho = [[0] * (T+1) for _ in range(2)]
summ = alpha[0][T] + alpha[1][T]
for t in range(1, T+1):
    for j in range(2):
        rho[j][t] = beta[j][t] * alpha[j][t] / summ
for i in range(2):
    for t in range(1, T+1):
        print(f'{rho[i][t]:.2f}', end=' ')
    print()
