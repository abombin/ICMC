for i in $(cat ../newdir.txt); do cd "$i"
	java -jar /home/ubuntu/trimmomatic/Trimmomatic-0.39/trimmomatic-0.39.jar PE \
	"$i"_R1.fastq.gz "$i"_R2.fastq.gz "$i"_R1_paired.fq.gz \
	"$i"_R1_unpaired.fq.gz "$i"_R2_paired.fq.gz "$i"_R2_unpaired.fq.gz \
	ILLUMINACLIP:/home/ubuntu/trimmomatic/Trimmomatic-0.39/adapters/TruSeq3-PE.fa:2:30:10:2:True \
	LEADING:3 TRAILING:3 SLIDINGWINDOW:4:15 MINLEN:36
	cd ../
done
