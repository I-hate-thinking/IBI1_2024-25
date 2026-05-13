import matplotlib.pyplot as plt
from collections import defaultdict
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(current_dir, "Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa")

target_stop = input("Enter stop codon (TAA/TAG/TGA): ").strip().upper()

seqs = []
current = ""
with open(filename, "r") as f:
    for line in f:
        line = line.strip()
        if line.startswith(">"):
            if current:
                seqs.append(current)
                current = ""
        else:
            current += line
    if current:
        seqs.append(current)

codon_counts = defaultdict(int)

for seq in seqs:
    best_orf = []
    for s in range(len(seq)-2):
        if seq[s:s+3] == "ATG":
            orf = []
            for i in range(s, len(seq)-2, 3):
                c = seq[i:i+3]
                if c == target_stop:
                    break
                orf.append(c)
            else:
                continue
            if len(orf) > len(best_orf):
                best_orf = orf
    for codon in best_orf:
        codon_counts[codon] += 1

print("\nCodon frequencies:")
for c, n in sorted(codon_counts.items()):
    print(c, n)

labels = list(codon_counts.keys())
sizes = list(codon_counts.values())

plt.figure(figsize=(8,8))
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title(f"Codon usage upstream of {target_stop}")
plt.savefig(os.path.join(current_dir, f"codon_pie_{target_stop}.png"), dpi=300)
plt.close()

print(f"\nPie chart saved as codon_pie_{target_stop}.png")