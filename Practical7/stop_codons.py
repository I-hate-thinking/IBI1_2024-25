import os
#identify genes containing termination codons and output the new FASTA format
current_dir = os.path.dirname(os.path.abspath(__file__))
infile = os.path.join(current_dir, "Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa")
outfile = os.path.join(current_dir, "stop_genes.fa")

def get_gene_name(header):
    return header.split()[0].replace(">", "")

current_seq = ""
current_header = ""
results = []

with open(infile, "r") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        if line.startswith(">"):
            if current_header and current_seq:
                seq = current_seq.replace("T", "U")
                stops = []
                if "ATG" in current_seq:
                    for i in range(0, len(seq)-2, 3):
                        c = seq[i:i+3]
                        if c == "UAA": stops.append("TAA")
                        if c == "UAG": stops.append("TAG")
                        if c == "UGA": stops.append("TGA")
                stops = sorted(list(set(stops)))
                if stops:
                    gene = get_gene_name(current_header)
                    new_head = f">{gene} {' '.join(stops)}"
                    results.append((new_head, current_seq))
            current_header = line
            current_seq = ""
        else:
            current_seq += line

#the last one
if current_header and current_seq:
    seq = current_seq.replace("T", "U")
    stops = []
    if "ATG" in current_seq:
        for i in range(0, len(seq)-2, 3):
            c = seq[i:i+3]
            if c == "UAA": stops.append("TAA")
            if c == "UAG": stops.append("TAG")
            if c == "UGA": stops.append("TGA")
    stops = sorted(list(set(stops)))
    if stops:
        gene = get_gene_name(current_header)
        new_head = f">{gene} {' '.join(stops)}"
        results.append((new_head, current_seq))

#output
with open(outfile, "w") as f:
    for h, s in results:
        f.write(h + "\n")
        f.write(s + "\n")

print("Done! Output to stop_genes.fa")