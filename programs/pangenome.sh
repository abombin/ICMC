conda activate bactopia

cd bactopia_gtdbtk
for i in $(cat ../bacteria.list); do cd ./"$i"
mkdir panOut

bactopia --wf pangenome \
--bactopia ./output \
--outdir ./panOut \
--max_cpus 16 | tee pangenome.log;

cd ../
done