# USAGE: python3 tped2nexus.py <prefixfile.tped>
# WARNING: This script is specifically designed for haploid genotypes

from sys import argv

tfam = argv[1] + '.tfam'
tped = argv[1] + '.tped'

ids = []
with open(tfam, 'r') as f:
    for line in f:
        ids.append(line.split(' ')[0]) 
sequences = {i:'' for i in range(len(ids))}
with open(tped, 'r') as f:
    for line in f: 
        for i in range(len(ids)): 
            column = (i * 2) + 4 
            sequences[i] += line.split(' ')[column] 

for i in range(len(ids)):
    print('>{}'.format(ids[i]))
    print(sequences[i])

