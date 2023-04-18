# USAGE: bash tped2fasta.sh <prefix_tped>
# WARNING: This script is specifically designed for haploid genotypes

prefx=$1
tped=$prefx.tped
tfam=$prefx.tfam
ncols=$(head -n 1 $tped | awk '{print NF}')

for col in $(seq 5 2 $ncols); do
	cut -d " " -f $col $tped | tr "\n" " " | sed 's/ //g' | sed 's/$/\n/g' >> $prefx.tmp
done
cut -d " " -f 1 $tfam | sed 's/^/>/g' | paste - $prefx.tmp | tr "\t" "\n"

rm $prefx.tmp
