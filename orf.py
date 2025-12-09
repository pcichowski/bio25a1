CODONS = {
    'TTT': 'F', 'TTC': 'F', 'TTA': 'L', 'TTG': 'L', 'CTT': 'L', 'CTC': 'L', 'CTA': 'L', 'CTG': 'L',
    'ATT': 'I', 'ATC': 'I', 'ATA': 'I', 'ATG': 'M', 'GTT': 'V', 'GTC': 'V', 'GTA': 'V', 'GTG': 'V',
    'TCT': 'S', 'TCC': 'S', 'TCA': 'S', 'TCG': 'S', 'AGT': 'S', 'AGC': 'S', 'CCT': 'P', 'CCC': 'P',
    'CCA': 'P', 'CCG': 'P', 'ACT': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T', 'GCT': 'A', 'GCC': 'A',
    'GCA': 'A', 'GCG': 'A', 'TAT': 'Y', 'TAC': 'Y', 'CAT': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
    'AAT': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K', 'GAT': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
    'TGT': 'C', 'TGC': 'C', 'TGG': 'W', 'CGT': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R', 'AGA': 'R',
    'AGG': 'R', 'GGT': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G', 'TAA': '*', 'TAG': '*', 'TGA': '*'
}

def reverse_complement(dna):
    complement = str.maketrans('ATCG','TAGC')
    return dna.translate(complement)[::-1]

def find_orfs_in_frame(seq):
    proteins = set()
    for i in range(len(seq)-2):
        if seq[i:i+3] == 'ATG':
            protein = ''
            for j in range(i, len(seq)-2, 3):
                codon = seq[j:j+3]
                aa = CODONS.get(codon,'')
                if aa == '*':
                    proteins.add(protein)
                    break
                protein += aa
    return proteins

def find_all_orfs(seq):
    frames = [seq[i:] for i in range(3)] + [reverse_complement(seq)[i:] for i in range(3)]
    all_proteins = set()
    for frame in frames:
        all_proteins.update(find_orfs_in_frame(frame))
    return all_proteins

def parse_fasta_file(filename):
    sequences = []
    seq = ''
    with open(filename,'r') as f:
        for line in f:
            line = line.strip()
            if line.startswith('>'):
                if seq:
                    sequences.append(seq)
                    seq = ''
            else:
                seq += line
        if seq:
            sequences.append(seq)
    return sequences

fasta_file = "input.txt"  
sequences = parse_fasta_file(fasta_file)

all_proteins = set()
for seq in sequences:
    all_proteins.update(find_all_orfs(seq))

for protein in all_proteins:
    print(protein)
