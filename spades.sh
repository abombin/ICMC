for i in $(cat ../newdir.txt); do cd "$i"
mkdir spades_out
/home/ubuntu/spades/SPAdes-3.15.4-Linux/bin/spades.py -1 "$i"_R1_paired.fq.gz -2 "$i"_R2_paired.fq.gz \
-o spades_out
cd ../
done
