from math import comb

def probability_at_least_N(k, N):
    n_offspring = 2**k
    p = 0.25

    total_prob = 0
    for i in range(N, n_offspring + 1):
        total_prob += comb(n_offspring, i) * (p**i) * ((1 - p)**(n_offspring - i))

    return total_prob

k, N = 7, 37
print(round(probability_at_least_N(k, N), 3))
