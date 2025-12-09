sequences = []
with open('input.txt', 'r') as f:
    current_seq = []
    for line in f:
        line = line.strip()
        if line.startswith('>'):
            if current_seq:
                sequences.append("".join(current_seq))
            current_seq = []
        else:
            current_seq.append(line)
    if current_seq:
        sequences.append("".join(current_seq))

n = len(sequences[0])
profile = {'A': [0]*n, 'C': [0]*n, 'G': [0]*n, 'T': [0]*n}

for seq in sequences:
    for i, char in enumerate(seq):
        profile[char][i] += 1

consensus = ""
for i in range(n):
    consensus += max("ACGT", key=lambda base: profile[base][i])

print(consensus)
for base in "ACGT":
    print(f"{base}: {' '.join(map(str, profile[base]))}")