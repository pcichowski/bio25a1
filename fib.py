def rabbit_pairs(n, k):
    F = [0] * (n + 1)
    F[1] = 1
    if n >= 2:
        F[2] = 1
    for i in range(3, n + 1):
        F[i] = F[i - 1] + k * F[i - 2]
    return F[n]

n, k = 31, 4
print(rabbit_pairs(n, k))
