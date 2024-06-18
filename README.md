# misc_tools
Miscelaneous scripts to parse, convert or manipulate various types of genomic data

## reverse_complement.py
Takes a fasta sequence as input and returns its reverse complement

## tped2fasta.py
Takes a tped file as input and converts it to a fasta representation

## tped2fasta.sh
Same as *tped2fasta.py* but faster

## tped2nexus.py
Takes a tped file as input and converts it to a nexus representation

## fasta2binary.py
Takes a pseudo-fasta file consiting of biallelic SNPs and returns a binary matrix in which Major alleles are codified as '0', minor alleles as '1' and missing data ('?') as the mean allele frequency. You can use this matrix to quickly compute a PCA

## dna2aa.py
This script uses the [Expasy server](https://web.expasy.org/translate/programmatic_access.html) to translate a nucleotide sequence into the 6 possible AA frames. 

## extract_read_from_fasta.py
Extract specific contgs from a fasta file
