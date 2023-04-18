#!/usr/bin/env python3

from sys import argv

inpf = argv[1]
if inpf == "-":
    inpf = '/dev/stdin'

pairs = {'A':'T','T':'A','C':'G','G':'C','N':'N','-':'-','?':'?'}

with open(inpf, 'r') as f:
    for line in f:
        if line.startswith('>'):
            try:
                print(''.join([pairs[n] for n in seq[::-1]]))
            except NameError:
                pass
            seq = ''
            print(line.strip() + '_REVCOMP')
        else:
            seq = seq + line.strip()
print(''.join([pairs[n] for n in seq[::-1]]))
