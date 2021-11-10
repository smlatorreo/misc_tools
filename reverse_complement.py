from Bio import Seq
from sys import argv

with open("%s" % argv[1]) as file:
    input = file.read().splitlines()

for i in input:
    sequence = Seq.Seq(i)
    print(sequence.reverse_complement())
