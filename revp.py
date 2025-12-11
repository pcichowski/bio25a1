def parse_fasta(lines):
    seqs = {}
    label = None
    buf = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        if line.startswith(">"):
            if label:
                seqs[label] = "".join(buf)
            label = line[1:]
            buf = []
        else:
            buf.append(line)
    if label:
        seqs[label] = "".join(buf)
    return seqs

def load_fasta_file(path):
    with open(path) as f:
        return parse_fasta(f)

def reverse_complement(s):
    complement = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
    return ''.join(complement[base] for base in reversed(s))

def find_reverse_palindromes(seq, min_len=4, max_len=12):
    results = []
    n = len(seq)
    for l in range(min_len, max_len+1):
        for i in range(n - l + 1):
            subseq = seq[i:i+l]
            if subseq == reverse_complement(subseq):
                results.append((i+1, l))
    return results

seqs = load_fasta_file("input.txt")
seq = list(seqs.values())[0]
palindromes = find_reverse_palindromes(seq)

for pos, l in palindromes:
    print(pos, l)
