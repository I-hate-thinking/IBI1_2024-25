import re
import os
from Bio import SeqIO
def find_tata_genes(input_file, output_file):
        """
    Identify genes containing the TATA box sequence (TATAWAW) and save them to a new file 
    """
        tata_pattern = re.compile(r'TATA[AT][AT]')  # TATAWAW model，W=A/T
        with open(output_file, 'w') as out_f:
             for record in SeqIO.parse(input_file, 'fasta'):
            # Retrieve gene name 
                 gene_name = record.description.split()[0]
            # Merge multiple lines into a single string and convert it to uppercase
                 sequence = str(record.seq).upper()
            # Search for the TATA box pattern
                 if tata_pattern.search(sequence):
                # write in new FASTA file
                    out_f.write(f'>{gene_name}\n')
            # Format the sequence in 80-character-per-line format
                    for i in range(0, len(sequence), 80):
                        out_f.write(sequence[i:i+80] + '\n')
if __name__ == "__main__":
    input_fasta = "R64-1-1.cdna.all.fa"
    output_fasta = "tata_genes.fa"
    
    print(f"Processing {input_fasta}...")
    find_tata_genes(input_fasta, output_fasta)
    print(f"Results saved to {output_fasta}")
