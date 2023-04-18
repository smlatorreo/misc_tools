from Bio import SeqIO
import pandas as pd
from sys import argv, stderr

fasta = argv[1]

seqs = {S.id:pd.Series(list(S.seq)) for S in SeqIO.parse(fasta, 'fasta')}
m = pd.concat(seqs.values(), axis=1)

seg_sites = []
only_gaps = []
non_seg_pos = ''
for i in range(m.shape[0]):
    unique = set(m.iloc[i,:])
    if '-' in unique:
        unique.remove('-')
    if len(unique) > 1:
        seg_sites.append(i)
    elif len(unique) == 0:
        only_gaps.append(i)
    else:
        non_seg_pos = non_seg_pos + list(unique)[0]
non_seg_counts = {n:non_seg_pos.count(n) for n in ('A','C','G','T')}

print('Total length (original sequence):', m.shape[0], file = stderr)
print('Number of sites with full missing information (full gaps):', len(only_gaps), file = stderr)
print('Effective total length (removing full gaps)):', m.shape[0] - len(only_gaps), file = stderr)
print('Segregating sites:', len(seg_sites), file = stderr)
print('Non-segregating sites:', len(non_seg_pos), file = stderr)
print('Non-segregating site counts:', non_seg_counts, file = stderr)

for S in seqs:
    print('>', S, sep = '')
    print(''.join(seqs[S][seg_sites]))

