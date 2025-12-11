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


def overlap_graph(seqs, k=3):
    items = list(seqs.items())
    for a, s in items:
        suf = s[-k:]
        for b, t in items:
            if a == b:
                continue
            if t.startswith(suf):
                print(a, b)


seqs = load_fasta_file("input.txt")
overlap_graph(seqs)
