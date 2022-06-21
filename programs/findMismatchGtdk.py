
import pandas as pd
df=pd.read_csv("data/gtdbtk.bac120.summary.tsv",sep='\t', converters={'user_genome': lambda x: str(x)})
   
def getGtdbSpec(df):
    phyDat=df[['classification']]
    splitPhyDat=phyDat['classification'].str.split(';', expand=True)
    splitPhyDatRen=splitPhyDat.rename(columns={splitPhyDat.columns[6]: 'Experiment_taxa'})
    expTax=splitPhyDatRen[['Experiment_taxa']]
    expTax['Experiment_taxa']=expTax['Experiment_taxa'].str.replace('s__', '')
    gtdbTax=pd.concat([df[['user_genome']], expTax], axis=1)
    return gtdbTax

print(getGtdbSpec(df))





