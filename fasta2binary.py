# Having a pseudo-fasta file consiting of biallelic SNPs, this script returns a binary matrix
# in which Major alleles are codified as '0', minor alleles as '1' and missing data ('?') as
# the mean allele frequency.
<<<<<<< HEAD
# If no imputation is needed, missing values can be passed as "nan". Just add the flag "--na".
# You can use this matrix to quickly compute a PCA
#
# USAGE: python fasta2binary.py [--nan] <file.fasta>
=======
# You can use this matrix to quickly compute a PCA
#
# USAGE: python fasta2binary.py <file.fasta>
>>>>>>> 9f2236446645e5e8328c351fdba96963c7f17849

from Bio import SeqIO
import pandas as pd
from sys import argv

<<<<<<< HEAD
fasta = argv[-1]
misschar = '?' # Change if required
na = False
if argv[1] == '--na':
    na = True
=======
fasta = argv[1]
misschar = '?' # Change if required
>>>>>>> 9f2236446645e5e8328c351fdba96963c7f17849

seqs = {S.id:pd.Series(list(S.seq)) for S in SeqIO.parse(fasta, 'fasta')}
m = pd.concat(seqs.values(), axis=1)

<<<<<<< HEAD
def binarize(pile, misschar, na):
=======
def binarize(pile, misschar):
>>>>>>> 9f2236446645e5e8328c351fdba96963c7f17849
    allele_counts = {allele:sum(pile == allele) for allele in set(pile)}
    max_freq = None
    M_allele = None
    for allele, freq in allele_counts.items():
        if allele != misschar:
            if max_freq is None or freq > max_freq:
                max_freq = freq
                M_allele = allele
    m_allele = list(set(allele_counts.keys()).difference(set((misschar , M_allele))))[0]
    N = len(pile) - sum(pile == misschar)
<<<<<<< HEAD
    if na == True:
        filler = 'nan'
    else:
        filler = sum(pile == m_allele) / N # Missing data is filled with the mean allele frequency
=======
    filler = sum(pile == m_allele) / N # Missing data is filled with the mean allele frequency
>>>>>>> 9f2236446645e5e8328c351fdba96963c7f17849
    bin_pile = pile.replace(M_allele, 0)
    bin_pile = bin_pile.replace(m_allele, 1)
    bin_pile = bin_pile.replace(misschar, filler)
    return(bin_pile)

<<<<<<< HEAD
print('\t'.join(list(seqs.keys())))
for pos in range(m.shape[0]):
    print('\t'.join([str(i) for i in binarize(m.iloc[pos,:], misschar, na)]))
=======
for pos in range(m.shape[0]):
    print('\t'.join([str(i) for i in binarize(m.iloc[pos,:], misschar)]))
>>>>>>> 9f2236446645e5e8328c351fdba96963c7f17849
