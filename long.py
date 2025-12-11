with open('input.txt') as f:
    data = f.read().splitlines()

reads = []
current = []
for line in data:
    if line.startswith('>'):
        if current: reads.append(''.join(current))
        current = []
    else:
        current.append(line)
if current: reads.append(''.join(current))

N = len(reads)
adj = {}

for i in range(N):
    s1 = reads[i]
    best_j = -1
    max_ov = -1

    for j in range(N):
        if i == j: continue
        s2 = reads[j]
        start_k = min(len(s1), len(s2))
        min_k = len(s1) // 2

        for k in range(start_k, min_k, -1):
            if k <= max_ov: break 
            if s1.endswith(s2[:k]):
                max_ov = k
                best_j = j
                break

    if best_j != -1:
        adj[i] = (best_j, max_ov)

targets = set(val[0] for val in adj.values())
start_node = next(i for i in range(N) if i not in targets)

result = reads[start_node]
curr = start_node
while curr in adj:
    nxt, overlap = adj[curr]
    result += reads[nxt][overlap:]
    curr = nxt

print(result)
