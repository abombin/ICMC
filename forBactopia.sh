for i in $(cat ../newdir.txt); do cd "$i"
	awk -F '\t' 'NR>1 {print $3}' ./data/camitax.tsv > bacteria.id
	sed -e "s/ /-/g" bacteria.id >bacteria.name
	cat bacteria.name | tr '[:upper:]' '[:lower:]' > bacteria.bucket
	bacteria=$(cat bacteria.bucket)
	mkdir -p ../../bactopia/"$bacteria"/input
	mv *.fastq.gz ../../bactopia/"$bacteria"/input/
	cp bacteria.* ../../bactopia/"$bacteria"/
	cd ../
done
