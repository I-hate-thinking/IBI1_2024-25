import matplotlib.pyplot as plt

# 1. Create a dictionary of gene expression
gene_exp = {
    "TP53": 12.4,
    "EGFR": 15.1,
    "BRCA1": 8.2,
    "PTEN": 5.3,
    "ESR1": 10.7
}
print("Initial gene expression dictionary:")
print(gene_exp)

# 2. add MYC
gene_exp["MYC"] = 11.6
print("\nAfter adding MYC:")
print(gene_exp)

# 3. produce the bar chart
genes = list(gene_exp.keys())
values = list(gene_exp.values())

plt.bar(genes, values, color='skyblue')
plt.title("Gene Expression Levels")
plt.xlabel("Gene")
plt.ylabel("Expression Level")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Create a variable representing a gene of interest
gene_of_interest = "TP53"  

if gene_of_interest in gene_exp:
    print(f"\n{gene_of_interest} expression: {gene_exp[gene_of_interest]}")
else:
    print(f"\nError: {gene_of_interest} is not in the dataset.")

# calculate the average
average = sum(values) / len(values)
print(f"\nAverage gene expression: {average:.2f}")