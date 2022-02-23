conda activate bactopia

# Initial set up step
mkdir input
mkdir process
mkdir bactopia

(cd ./input && ls *_1.fastq.gz) > inputList.txt

cat inputList.txt |cut -f1 -d"_" > newdir.txt



for i in $(cat newdir.txt); do mkdir process/"$i"; cp ./input/"$i"* ./process/"$i"/; done

cd process

 Trim and filter the sequences
sh ../programs/trimmomatic.sh
sh ../programs/spades.sh
sh ../programs/camitax.sh
sh ../programs/forBactopia.sh

cd ../

sh ./programs/bactopia.sh

sh ./programs/packTransfer.sh


