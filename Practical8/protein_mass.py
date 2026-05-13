# 氨基酸残基质量表
aa_mass = {
    'G': 57.02,
    'A': 71.04,
    'S': 87.03,
    'P': 97.05,
    'V': 99.07,
    'T': 101.05,
    'C': 103.01,
    'I': 113.08,
    'L': 113.08,
    'N': 114.04,
    'D': 115.03,
    'Q': 128.06,
    'K': 128.09,
    'E': 129.04,
    'M': 131.04,
    'H': 137.06,
    'F': 147.07,
    'R': 156.10,
    'Y': 163.06,
    'W': 186.08
}

def protein_mass(sequence):
    """
    输入氨基酸序列，返回蛋白质分子量（amu）
    含未知氨基酸时返回错误信息
    """
    total = 0.0
    for aa in sequence:
        if aa not in aa_mass:
            return f"Error: unknown amino acid '{aa}'"
        total += aa_mass[aa]
    return round(total, 2)

# 示例调用（作业要求必须有）
if __name__ == "__main__":
    seq_example = "MALWMRLL"
    mass = protein_mass(seq_example)
    print(f"Sequence: {seq_example}")
    print(f"Protein mass: {mass} amu")