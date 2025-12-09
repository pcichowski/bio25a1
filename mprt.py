import requests

with open('input.txt', 'r') as f:
    for line in f:
        raw_id = line.strip()
        if not raw_id:
            continue

        accession = raw_id.split('_')[0]
        response = requests.get(f"http://www.uniprot.org/uniprot/{accession}.fasta")
        
        sequence = "".join(response.text.splitlines()[1:])

        locations = []
        for i in range(len(sequence) - 3):
            if (sequence[i] == 'N' and 
                sequence[i+1] != 'P' and 
                sequence[i+2] in 'ST' and 
                sequence[i+3] != 'P'):
                locations.append(str(i + 1))

        if locations:
            print(raw_id)
            print(" ".join(locations))