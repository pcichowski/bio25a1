CODONS = {
    'UUU':'F','UUC':'F','UUA':'L','UUG':'L','CUU':'L','CUC':'L','CUA':'L','CUG':'L',
    'AUU':'I','AUC':'I','AUA':'I','AUG':'M','GUU':'V','GUC':'V','GUA':'V','GUG':'V',
    'UCU':'S','UCC':'S','UCA':'S','UCG':'S','AGU':'S','AGC':'S','CCU':'P','CCC':'P',
    'CCA':'P','CCG':'P','ACU':'T','ACC':'T','ACA':'T','ACG':'T','GCU':'A','GCC':'A',
    'GCA':'A','GCG':'A','UAU':'Y','UAC':'Y','CAU':'H','CAC':'H','CAA':'Q','CAG':'Q',
    'AAU':'N','AAC':'N','AAA':'K','AAG':'K','GAU':'D','GAC':'D','GAA':'E','GAG':'E',
    'UGU':'C','UGC':'C','UGG':'W','CGU':'R','CGC':'R','CGA':'R','CGG':'R','AGA':'R',
    'AGG':'R','GGU':'G','GGC':'G','GGA':'G','GGG':'G','UAA':'_','UAG':'_','UGA':'_'
}

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

def remove_introns(dna, introns):
    for intron in introns:
        dna = dna.replace(intron,'')
    return dna

def transcribe(dna):
    return dna.replace('T','U')

def translate(rna):
    protein = ''
    for i in range(0,len(rna)-2,3):
        codon = rna[i:i+3]
        aa = CODONS.get(codon,'')
        if aa == '_':
            break
        protein += aa
    return protein

fasta_file = 'input.txt'
sequences = parse_fasta_file(fasta_file)

main_dna = sequences[0]
introns = sequences[1:]

exons = remove_introns(main_dna,introns)
rna = transcribe(exons)
protein = translate(rna)
print(protein)

