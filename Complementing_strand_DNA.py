# st = "AAAACCCGGT"
# st = st.replace('A', 't').replace('T', 'a').replace('C', 'g').replace('G', 'c').upper()[::-1]
# print (st)

DNA= input("Pleae inster the DNA sequence: ") # getting the DNA-seq

# we need to get the complement seq
# reverse it
# print reverse-complement seq

def complement (DNA):
    comp= {"A":"T", "G":"C", "T":"A", "C":"G"}
    compDNA = ''
    for i in comp:
        compDNA+= comp[i]
    return compDNA

def reverse (DNA): 
    return DNA [::-1]

def reverse_complement (DNA):
    compDNA = complement(DNA)
    revcomp = reverse (compDNA)
    return revcomp

print(reverse_complement(DNA))