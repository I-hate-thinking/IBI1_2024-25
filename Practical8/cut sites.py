def find_restriction_sites(dna_sequence, recognition_sequence):    
    # verify whether two sequences only contain standard nucleotides
    valid_nucleotides = {'A', 'C', 'G', 'T'}   
    # check the DNA sequence
    if not all(nuc in valid_nucleotides for nuc in dna_sequence.upper()):
        raise ValueError("The DNA sequence contains non-standard nucleotides (only allowing A, C, G, T).")   
    # check the recognition sequence
    if not all(nuc in valid_nucleotides for nuc in recognition_sequence.upper()):
        raise ValueError("The recognition sequence contains non-standard nucleotides (only A, C, G and T are allowed).")   
    # convert to uppercase to ensure case insensitivity
    dna_upper = dna_sequence.upper()
    recog_upper = recognition_sequence.upper()  
    # search for all matching loci
    sites = []
    recog_length = len(recog_upper)
    seq_length = len(dna_upper)
    for i in range(seq_length - recog_length + 1):
        if dna_upper[i:i+recog_length] == recog_upper:
            sites.append(i)  # 0-based indexes
    return sites

# example
if __name__ == "__main__":
    try:
        # example1: EcoRI(GAATTC)
        dna_seq1 = "ATCGAATTCTAGGAATTCGG"
        enzyme_seq1 = "GAATTC"
        print(f"DNA sequence: {dna_seq1}")
        print(f"recognition sequence: {enzyme_seq1}")
        print("cleavage site:", find_restriction_sites(dna_seq1, enzyme_seq1))       
        # example2: BamHI(GGATCC)
        dna_seq2 = "AGCTGGATCCTAGGTGGATCCAA"
        enzyme_seq2 = "GGATCC"
        print(f"\nDNA sequence: {dna_seq2}")
        print(f"recognition sequence: {enzyme_seq2}")
        print("cleavage site:", find_restriction_sites(dna_seq2, enzyme_seq2))        
        # example3: invalid sequence (containing non-standard nucleotides)
        dna_seq3 = "AGCTXGATC"
        enzyme_seq3 = "GATC"
        print("\nattempted invalid sequence:")
        print("cleavage site:", find_restriction_sites(dna_seq3, enzyme_seq3))
        # will lead to ValueError    
    except ValueError as e:
        print(f"error: {e}")