with open("rosalind_rna.txt") as f:
   dna = f.read()


dna = dna.replace("T", "U")

print(dna)
