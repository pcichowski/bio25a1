import matplotlib.pyplot as plt

# ---------------------------------------
# Reverse complement
# ---------------------------------------
def revcomp(seq):
    comp = str.maketrans('ACGT', 'TGCA')
    return seq.translate(comp)[::-1]

# ---------------------------------------
# Generate 6 reading frames
# ---------------------------------------
def frames(seq):
    rc = revcomp(seq)
    return [
        seq[0:], seq[1:], seq[2:],        # +1 +2 +3
        rc[0:],  rc[1:],  rc[2:]          # -1 -2 -3
    ]

# ---------------------------------------
# Find ORFs in a single frame
# ---------------------------------------
def find_orfs_in_frame(frame):
    starts = []
    orfs = []
    i = 0
    L = len(frame)
    stops = {"TAA","TAG","TGA"}

    while i < L-2:
        codon = frame[i:i+3]
        if codon == "ATG":
            starts.append(i)
            i += 3
            continue
        if codon in stops:
            for s in starts:
                if (i - s) % 3 == 0:
                    orfs.append((s, i+3))
            starts = []
            i += 3
            continue
        i += 3
    return orfs

# ---------------------------------------
# Translate nucleotide ORF to protein
# ---------------------------------------
codon_table = {
"ATA":"I","ATC":"I","ATT":"I","ATG":"M",
"ACA":"T","ACC":"T","ACG":"T","ACT":"T",
"AAC":"N","AAT":"N","AAA":"K","AAG":"K",
"AGC":"S","AGT":"S","AGA":"R","AGG":"R",
"CTA":"L","CTC":"L","CTG":"L","CTT":"L",
"CCA":"P","CCC":"P","CCG":"P","CCT":"P",
"CAC":"H","CAT":"H","CAA":"Q","CAG":"Q",
"CGA":"R","CGC":"R","CGG":"R","CGT":"R",
"GTA":"V","GTC":"V","GTG":"V","GTT":"V",
"GCA":"A","GCC":"A","GCG":"A","GCT":"A",
"GAC":"D","GAT":"D","GAA":"E","GAG":"E",
"GGA":"G","GGC":"G","GGG":"G","GGT":"G",
"TCA":"S","TCC":"S","TCG":"S","TCT":"S",
"TTC":"F","TTT":"F","TTA":"L","TTG":"L",
"TAC":"Y","TAT":"Y","TAA":"*","TAG":"*",
"TGC":"C","TGT":"C","TGA":"*","TGG":"W"
}

def translate(seq):
    out = []
    for i in range(0, len(seq), 3):
        codon = seq[i:i+3]
        if len(codon) < 3:
            break
        aa = codon_table.get(codon, 'X')
        if aa == '*':
            break
        out.append(aa)
    return ''.join(out)

# ---------------------------------------
# Main ORF finder
# ---------------------------------------
def find_all_orfs(seq, min_nt=100):
    all_orfs = []
    frs = frames(seq)

    for fi, fr in enumerate(frs):
        orf_coords = find_orfs_in_frame(fr)
        for start, end in orf_coords:
            nt = fr[start:end]
            if len(nt) >= min_nt:
                aa = translate(nt)
                all_orfs.append((fi+1, start, end, aa))

    unique = {}
    for fr, s, e, aa in all_orfs:
        unique[aa] = (fr, s, e, aa)

    return list(unique.values())


# ---------------------------------------
# Read input from file input.txt
# ---------------------------------------
with open("input.txt") as f:
    seq = "".join(line.strip() for line in f if not line.startswith(">"))

orfs = find_all_orfs(seq)
lengths = [len(x[3]) for x in orfs]
print(lengths)

# Histogram
plt.hist(lengths, bins=range(0, max(lengths)+10, 10), edgecolor='black')
plt.xlabel("Długość ORF (aminokwasy)")
plt.ylabel("Liczba")
plt.title("Histogram długości ORF")
plt.xticks(range(0, max(lengths)+10, 10))
plt.show()

# Scatter
plt.scatter(range(len(lengths)), lengths)
plt.xlabel("Numer ORF")
plt.ylabel("Długość białka")
plt.title("Długość ORF-ów")
plt.show()

print("Liczba ORF-ów:", len(orfs))
print("Najdłuższy:", max(lengths) if lengths else 0)
