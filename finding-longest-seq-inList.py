dna = ["ATTCC","GGGGGCCCCAAAA", "GTTCCAA", "AATTAAA", "GGGGGCCCC"]
#find the longest one in the list
total_dna = len(dna)
print(total_dna)

longest = 0
index = 0
total_data= len(dna)

while index < total_data:
    current = len(dna[index])
    if current > longest:
        longest= current
        longest_segment = dna[index]
    index+=1
print(longest, longest_segment)