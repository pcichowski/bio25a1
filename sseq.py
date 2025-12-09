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

s, t = sequences[0], sequences[1]
indices = []
current_pos = 0

for symbol in t:
    found_at = s.find(symbol, current_pos)
    indices.append(str(found_at + 1))
    current_pos = found_at + 1

print(" ".join(indices))