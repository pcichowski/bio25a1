with open("rosalind_hamm.txt") as f:
   lines = f.readlines()

# dna1 = "GAGCCTACTAACGGGAT"
# dna2 = "CATCGTAATGACGGCCT"
dna1 = lines[0]
dna2 = lines[1]

cnt = 0

for a, b in zip(dna1, dna2):
   if a != b:
      cnt += 1

print(cnt)
