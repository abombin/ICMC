conda activate bactopia

(cd ./input && ls *_R1.fastq.gz) > inputList.txt

cat inputList.txt |cut -f1 -d"_" > newdir.txt

mkdir process

for i in $(cat newdir.txt); do mkdir process/"$i"; cp ./input/"$i"* ./process/"$i"/; done


cd process

sh ../programs/trimmomatic.sh
sh ../programs/spades.sh
sh ../programs/camitax.sh
sh ../programs/forBactopia.sh

cd ../

sh ./programs/bactopia.sh

sh ./programs/packTransfer.sh


