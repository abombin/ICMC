for i in $(cat newdir.txt); do
if [ -f ./gtdbtk/input/"$i".fasta ]; then
    echo "$i exists" >> ./gtdbtk/completeSpades.txt
else 
    echo "$i does failed." >> ./gtdbtk/failedSpades.txt
fi
done
