pam250_str = """
    A  C  D  E  F  G  H  I  K  L  M  N  P  Q  R  S  T  V  W  Y
A  2 -2  0  0 -3  1 -1 -1 -1 -2 -1  0  1  0 -2  1  1  0 -6 -3
C -2 12 -5 -5 -4 -3 -3 -2 -5 -6 -5 -4 -3 -5 -4  0 -2 -2 -8  0
D  0 -5  4  3 -6  1  1 -2  0 -4 -3  2 -1  2 -1  0  0 -2 -7 -4
E  0 -5  3  4 -5  0  1 -2  0 -3 -2  1 -1  2 -1  0  0 -2 -7 -4
F -3 -4 -6 -5  9 -5 -2  1 -5  2  0 -3 -5 -5 -4 -3 -3 -1  0  7
G  1 -3  1  0 -5  5 -2 -3 -2 -4 -3  0  0 -1 -3  1  0 -1 -7 -5
H -1 -3  1  1 -2 -2  6 -2  0 -2 -2  2  0  3  2 -1 -1 -2 -3  0
I -1 -2 -2 -2  1 -3 -2  5 -2  2  2 -2 -2 -2 -2 -1  0  4 -5 -1
K -1 -5  0  0 -5 -2  0 -2  5 -3  0  1 -1  1  3  0  0 -2 -3 -4
L -2 -6 -4 -3  2 -4 -2  2 -3  6  4 -3 -3 -2 -3 -3 -2  2 -2 -1
M -1 -5 -3 -2  0 -3 -2  2  0  4  6 -2 -2 -1  0 -2 -1  2 -4 -2
N  0 -4  2  1 -3  0  2 -2  1 -3 -2  2  0  1  0  1  0 -2 -4 -2
P  1 -3 -1 -1 -5  0  0 -2 -1 -3 -2  0  6  0  0  1  0 -1 -6 -5
Q  0 -5  2  2 -5 -1  3 -2  1 -2 -1  1  0  4  1 -1 -1 -2 -5 -4
R -2 -4 -1 -1 -4 -3  2 -2  3 -3  0  0  0  1  6  0 -1 -2  2 -4
S  1  0  0  0 -3  1 -1 -1  0 -3 -2  1  1 -1  0  2  1 -1 -2 -3
T  1 -2  0  0 -3  0 -1  0  0 -2 -1  0  0 -1 -1  1  3  0 -5 -3
V  0 -2 -2 -2 -1 -1 -2  4 -2  2  2 -2 -1 -2 -2 -1  0  4 -6 -2
W -6 -8 -7 -7  0 -7 -3 -5 -3 -2 -4 -4 -6 -5  2 -2 -5 -6 17  0
Y -3  0 -4 -4  7 -5  0 -1 -4 -1 -2 -2 -5 -4 -4 -3 -3 -2  0 10
"""

lines = pam250_str.strip().split('\n')
aa_cols = lines[0].split()
scores = {}
for line in lines[1:]:
    parts = line.split()
    row_aa = parts[0]
    vals = list(map(int, parts[1:]))
    for col_aa, val in zip(aa_cols, vals):
        scores[(row_aa, col_aa)] = val

with open('input.txt', 'r') as f:
    content = f.read().strip()

parts = content.split('>')
seqs = []
for p in parts:
    if not p: continue
    lines = p.split('\n', 1)
    if len(lines) > 1:
        seqs.append(lines[1].replace('\n', '').strip())
        
s = seqs[0]
t = seqs[1]
n = len(s)
m = len(t)

dp = [[0] * (m + 1) for _ in range(n + 1)]
max_score = -1
max_pos = (0, 0)
gap = 5

for i in range(1, n + 1):
    for j in range(1, m + 1):
        match = dp[i-1][j-1] + scores[(s[i-1], t[j-1])]
        delete = dp[i-1][j] - gap
        insert = dp[i][j-1] - gap
        val = max(0, match, delete, insert)
        dp[i][j] = val
        if val > max_score:
            max_score = val
            max_pos = (i, j)

i, j = max_pos
while dp[i][j] != 0:
    val = dp[i][j]
    score_match = scores[(s[i-1], t[j-1])]
    
    if i > 0 and j > 0 and val == dp[i-1][j-1] + score_match:
        i -= 1
        j -= 1
    elif i > 0 and val == dp[i-1][j] - gap:
        i -= 1
    else:
        j -= 1
        
res_s = s[i:max_pos[0]]
res_t = t[j:max_pos[1]]

output = f"{max_score}\n{res_s}\n{res_t}"
print(output)

with open('output.txt', 'w') as f:
    f.write(output)

