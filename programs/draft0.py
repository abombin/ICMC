import pandas as pd

#gtdbDat=pd.read_csv('C:/Users/abomb/OneDrive - Emory University/bacteria/data/gtdb/bac120_metadata_r207.tsv', sep='\t')

#gtdbTax=gtdbDat[['accession', 'gtdb_taxonomy', 'ncbi_organism_name']]

#pd.DataFrame.to_csv(gtdbTax, 'bac120_metadata_r207Filtr.tsv', index=False, sep='\t')

gtdbDat=pd.read_csv('C:/Users/abomb/OneDrive - Emory University/bacteria/data/gtdb/bac120_metadata_r207Filtr.tsv', sep='\t')

sample=gtdbDat.loc[gtdbDat['gtdb_taxonomy']=='d__Bacteria;p__Proteobacteria;c__Gammaproteobacteria;o__Enterobacterales;f__Enterobacteriaceae;g__Serratia;s__Serratia marcescens_B']

print(sample.head(10))