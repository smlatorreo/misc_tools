# USAGE: python dna2aa.py <sequence[s].fasta>
# This script uses the Expasy server: https://web.expasy.org/translate/programmatic_access.html
import requests
from Bio import SeqIO
from sys import argv

inp = argv[1]

def translate(seq):
    data = {'dna_sequence':str(seq), 'output_format':'fasta'}
    response = requests.post('https://web.expasy.org/cgi-bin/translate/dna2aa.cgi', data=data)
    if response.status_code == 200:
        out = response.content.decode('utf-8')
    else:
        out = 'Error'
    return out

for record in SeqIO.parse(inp, 'fasta'):
    print('>{}'.format(record.id))
    print(record.seq)
    print(translate(record.seq))
