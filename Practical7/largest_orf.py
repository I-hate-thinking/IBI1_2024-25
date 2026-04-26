#find the largest open reading frame
seq = 'AAGAUACAUGCAAGUGGUGUGUCUGUUCUGAGAGGGCCUAAAAG'

#termination codon
stop_codons = {'UAA', 'UAG', 'UGA'}
orfs = []

#all possible starting positions
for i in range(len(seq) - 2):
    codon = seq[i:i+3]
    if codon == 'AUG':
        #look for the end
        length = 0
        for j in range(i, len(seq)-2, 3):
            c = seq[j:j+3]
            if c in stop_codons:
                length = j - i
                break
        if length > 0:
            orfs.append((length, seq[i:i+length]))

#find the largest
if orfs:
    longest = max(orfs, key=lambda x: x[0])
    print("Longest ORF sequence:", longest[1])
    print("Length (nt):", longest[0])
else:
    print("No ORF found.")