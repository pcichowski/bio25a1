import matplotlib.pyplot as plt

def read_fasta(filename):
    sequences = {}
    with open(filename) as f:
        seq_id = None
        seq_lines = []
        for line in f:
            line = line.strip()
            if line.startswith(">"):
                if seq_id:
                    sequences[seq_id] = "".join(seq_lines)
                seq_id = line[1:]
                seq_lines = []
            else:
                seq_lines.append(line)
        if seq_id:
            sequences[seq_id] = "".join(seq_lines)
    return list(sequences.values())

def global_alignment(seq1, seq2, match=1, mismatch=-1, gap=-2):
    n, m = len(seq1), len(seq2)

    # Score matrix
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # Initialize
    for i in range(n + 1):
        dp[i][0] = i * gap
    for j in range(m + 1):
        dp[0][j] = j * gap

    # Fill matrix
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if seq1[i-1] == seq2[j-1]:
                score = match
            else:
                score = mismatch
            
            dp[i][j] = max(
                dp[i-1][j-1] + score,
                dp[i-1][j] + gap,
                dp[i][j-1] + gap
            )

    # Backtracking
    align1, align2 = [], []
    i, j = n, m

    while i > 0 or j > 0:
        if i > 0 and j > 0:
            if seq1[i-1] == seq2[j-1]:
                score = match
            else:
                score = mismatch
            
            if dp[i][j] == dp[i-1][j-1] + score:
                align1.append(seq1[i-1])
                align2.append(seq2[j-1])
                i -= 1
                j -= 1
                continue

        if i > 0 and dp[i][j] == dp[i-1][j] + gap:
            align1.append(seq1[i-1])
            align2.append('-')
            i -= 1
        elif j > 0:
            align1.append('-')
            align2.append(seq2[j-1])
            j -= 1

    align1 = ''.join(reversed(align1))
    align2 = ''.join(reversed(align2))

    return dp[n][m], align1, align2

def calculate_stats(align1, align2):
    length = len(align1)
    identical = sum(1 for a, b in zip(align1, align2) if a == b and a != '-')
    gaps = sum(1 for a, b in zip(align1, align2) if a == '-' or b == '-')
    identity = (identical / length) * 100 if length > 0 else 0

    # Count gap regions
    gap_count = 0
    in_gap = False
    for a, b in zip(align1, align2):
        if a == '-' or b == '-':
            if not in_gap:
                gap_count += 1
                in_gap = True
        else:
            in_gap = False

    return {
        'length': length,
        'identity': identity,
        'gaps': gaps,
        'gap_count': gap_count
    }

def print_alignment(align1, align2, width=60):
    middle = []
    for a, b in zip(align1, align2):
        if a == b:
            middle.append('|')
        elif a == '-' or b == '-':
            middle.append(' ')
        else:
            middle.append('.')

    middle = ''.join(middle)

    for i in range(0, len(align1), width):
        print(align1[i:i+width])
        print(middle[i:i+width])
        print(align2[i:i+width])
        print()

def create_dotplot(seq1, seq2):
    xs, ys = [], []

    for i, char1 in enumerate(seq1):
        for j, char2 in enumerate(seq2):
            if char1 == char2:
                xs.append(i)
                ys.append(j)

    plt.figure(figsize=(10, 10))
    plt.scatter(xs, ys, s=1, c='blue', alpha=0.5)
    plt.xlabel('Pozycja w sekwencji 1')
    plt.ylabel('Pozycja w sekwencji 2')
    plt.title('Zgodne pozycje między sekwencjami')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('Figure_1.png', dpi=300)
    plt.show()

sequences = read_fasta('input.txt')
seq1, seq2 = sequences[0], sequences[1]

score, align1, align2 = global_alignment(seq1, seq2)
stats = calculate_stats(align1, align2)

print(f"Score dopasowania: {score}")
print(f"Długość alignmentu: {stats['length']}")
print(f"Procent identyczności: {stats['identity']:.2f}%")
print(f"Liczba luk: {stats['gaps']}")
print(f"Liczba ciągów luk: {stats['gap_count']}\n")

print_alignment(align1[:180], align2[:180])

create_dotplot(seq1, seq2)
