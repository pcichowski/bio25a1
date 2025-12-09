with open("rosalind_gc.txt") as f:
    input = f.read()

input = input.split(">")[1:]

dnas = []

for i in input:
    id = i[:13]
    dna = i[13:].replace("\n", "")
    percent = (dna.count("C") + dna.count("G")) / len(dna) * 100
    dnas.append((id, percent))

dnas.sort(key=lambda x: x[1], reverse=True)

print(dnas[0][0])
print(dnas[0][1])