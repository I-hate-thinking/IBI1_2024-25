seq = 'ATGCAAGTGGTGTGTCTGTTCTGAGAGGGCCTAA'
donor="GT"
accepyor="AG"
max_intron_length=0
#define the sequence of GT and AG
for i in range(len(seq)-1):
    if seq[i:i+2]==donor: #find all the donor site
        for j in range(i+2,len(seq)-1): #find the receptor site that is the closest to the donor site
            intron_length=j-i+2 #calculate the length of introns
            if intron_length>max_intron_length:
                max_intron_length=intron_length
            break
print(f"The largest intron is {max_intron_length}")