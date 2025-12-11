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


def longest_common_substring(seqs):
    strings = list(seqs.values())
    s0 = min(strings, key=len)
    length = len(s0)

    for l in range(length, 0, -1):
        for i in range(length - l + 1):
            substr = s0[i:i + l]
            if all(substr in s for s in strings):
                return substr
    return ""


seqs = load_fasta_file("input.txt")
print(longest_common_substring(seqs))
