s1='GAGCCTACTAACGGGAT'
s2='CATCGTAATGACGGCCT'
def hamingdistance(s1,s2):
    h=0
    for i in range(len(s1)):
        if s1[i]!=s2[i]:
            h+=1
    return(h)
print(hamingdistance(s1,s2))