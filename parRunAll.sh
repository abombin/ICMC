
sh ./programs/prepData.sh

cd process_par; ls -d */ | parallel -j 20 'cd {} && sh ../../programs/trimgalore.sh'; cd ../

echo "Finished Trimgalore"

sleep 120s


cd process_par; ls -d */ | parallel -j 4 'cd {} && sh ../../programs/parSpades.sh'; cd ../

echo "Finished Spades"
sleep 120s


bash -i ./programs/gtdbtk.sh

echo "Finished GTDB-Tk"

Rscript --vanilla ./programs/findMismatchGtdk.R

bash -i ./programs/forBactopiaGtdbtk.sh

bash -i ./programs/bactopia.sh

echo "Finished Bactopia Run"
sleep 120s

bash -i ./programs/pangenome.sh

sh ./programs/pack.sh

sh ./programs/transferAws.sh









