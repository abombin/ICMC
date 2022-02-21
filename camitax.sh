for i in $(cat ../newdir.txt); do cd "$i"
	mkdir input
	cp spades_out/contigs.fasta ./input/"$i".fasta
	/home/ubuntu/nextflow/nextflow run CAMI-challenge/CAMITAX -profile docker --db /home/ubuntu/camitax/db \
		--i ./input --x fasta
	cd ../
done
