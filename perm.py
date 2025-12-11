from itertools import permutations

n = 7

all_perms = list(permutations(range(1, n + 1)))

with open("output.txt", "w") as f:
    f.write(f"{len(all_perms)}\n")
    for p in all_perms:
        f.write(" ".join(map(str, p)) + "\n")
