from collections import Counter

with open("rosalind_dna.txt") as f:
    dna = f.read()

#dna = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"

cnts = Counter(dna)

print(cnts["A"], cnts["C"], cnts["G"], cnts["T"])