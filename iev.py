def expected_dominant(a, b, c, d, e, f):
    probs = [1, 1, 1, 0.75, 0.5, 0]
    counts = [a, b, c, d, e, f]

    per_couple_expected = sum(c * p for c, p in zip(counts, probs))

    return 2 * per_couple_expected

data = [18418, 17078, 18561, 19847, 19312, 18331]
print(expected_dominant(*data))
