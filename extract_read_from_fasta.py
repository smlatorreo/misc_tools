# Outputs to STDOUT
# Usage: extract_read_from_fasta.py <reads.fasta> <id>
# With a list of contigs: extract_read_from_fasta.py <reads.fasta> -l <contigs.list>
# Interactive mode: extract_read_from_fasta.py <reads.fasta> -i
from Bio import SeqIO
from sys import argv
from sys import stdout

if '-i' in argv:
    for read in SeqIO.parse("%s" % argv[1], "fasta"):
        print(read.id)
    match = input('Enter the first characters of the read you want to extract: ')
    output = input('Enter the name of the output file: ')
    for read in SeqIO.parse("%s" % argv[1], "fasta"):
        if read.id == match:
            SeqIO.write(read, output, "fasta")
elif '-l' in argv:
    lst_f = argv[-1]
    contigs = [i.strip() for i in open(lst_f, 'r').readlines()]
    for read in SeqIO.parse("%s" % argv[1], "fasta"):
        if read.id in contigs:
            SeqIO.write(read, stdout, "fasta")
else:
    for read in SeqIO.parse("%s" % argv[1], "fasta"):
        if read.id == argv[2]:
            SeqIO.write(read, stdout, "fasta")
