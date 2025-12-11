import blosum as bl

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

s, t = read_fasta("input.txt")
matrix = bl.BLOSUM(62)
gap = 5

m, n = len(s), len(t)
dp = [[0]*(n+1) for _ in range(m+1)]

for i in range(1, m+1):
    dp[i][0] = dp[i-1][0] - gap
for j in range(1, n+1):
    dp[0][j] = dp[0][j-1] - gap

for i in range(1, m+1):
    for j in range(1, n+1):
        match = dp[i-1][j-1] + matrix[s[i-1]][t[j-1]]
        delete = dp[i-1][j] - gap
        insert = dp[i][j-1] - gap
        dp[i][j] = max(match, delete, insert)

print(int(dp[m][n]))
