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

def edit_distance_alignment(s, t):
    m, n = len(s), len(t)
    dp = [[0]*(n+1) for _ in range(m+1)]
    back = [[None]*(n+1) for _ in range(m+1)]

    for i in range(1, m+1):
        dp[i][0] = i
        back[i][0] = 'U'
    for j in range(1, n+1):
        dp[0][j] = j
        back[0][j] = 'L'

    for i in range(1, m+1):
        for j in range(1, n+1):
            if s[i-1] == t[j-1]:
                dp[i][j] = dp[i-1][j-1]
                back[i][j] = 'D'
            else:
                options = [(dp[i-1][j-1]+1, 'D'), (dp[i-1][j]+1, 'U'), (dp[i][j-1]+1, 'L')]
                dp[i][j], back[i][j] = min(options, key=lambda x:x[0])

    i, j = m, n
    s_align, t_align = [], []
    while i > 0 or j > 0:
        if back[i][j] == 'D':
            s_align.append(s[i-1])
            t_align.append(t[j-1])
            i -= 1
            j -= 1
        elif back[i][j] == 'U':
            s_align.append(s[i-1])
            t_align.append('-')
            i -= 1
        elif back[i][j] == 'L':
            s_align.append('-')
            t_align.append(t[j-1])
            j -= 1

    return dp[m][n], ''.join(reversed(s_align)), ''.join(reversed(t_align))

s, t = read_fasta("input.txt")
dist, s_aln, t_aln = edit_distance_alignment(s, t)
print(dist)
print(s_aln)
print(t_aln)
