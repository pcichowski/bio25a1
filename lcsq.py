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

def longest_common_subsequence(s, t):
    m, n = len(s), len(t)
    dp = [[""] * (n+1) for _ in range(m+1)]

    for i in range(m):
        for j in range(n):
            if s[i] == t[j]:
                dp[i+1][j+1] = dp[i][j] + s[i]
            else:
                dp[i+1][j+1] = dp[i+1][j] if len(dp[i+1][j]) > len(dp[i][j+1]) else dp[i][j+1]

    return dp[m][n]


s, t = read_fasta("input.txt")
lcs = longest_common_subsequence(s, t)
print(lcs)
