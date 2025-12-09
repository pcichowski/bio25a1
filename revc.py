with open("rosalind_revc.txt") as f:
   dna = f.read()

#dna = "AAAACCCGGT"
dna = dna[::-1]

output = ""

for c in dna:
    if c == "A":
        output += "T"
    if c == "T":
        output += "A"
    if c == "C":
        output += "G"
    if c == "G":
        output += "C"

print(output)
