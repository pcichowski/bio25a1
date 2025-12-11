def dominant_phenotype_prob(k, m, n):
    total = k + m + n
    pk = k / total
    pm = m / total
    pn = n / total

    def p2(count):
        return count / (total - 1)

    p_KK = pk * p2(k - 1)

    p_KM = pk * p2(m)
    p_MK = pm * p2(k)

    p_KN = pk * p2(n)
    p_NK = pn * p2(k)

    p_MM = pm * p2(m - 1) * 0.75

    p_MN = pm * p2(n) * 0.5
    p_NM = pn * p2(m) * 0.5

    return p_KK + p_KM + p_MK + p_KN + p_NK + p_MM + p_MN + p_NM

print(dominant_phenotype_prob(17, 28, 16))
