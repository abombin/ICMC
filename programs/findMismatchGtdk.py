
import pandas as pd
df=pd.read_csv("data/gtdbtk.bac120.summary.tsv",sep='\t', converters={'user_genome': lambda x: str(x)})
metadat=pd.read_csv("data/metaDat.csv", converters={'uuid': lambda x: str(x)})
   
# get gtdbtk species names
def getGtdbSpec(df):
    phyDat=df[['classification']]
    splitPhyDat=phyDat['classification'].str.split(';', expand=True)
    splitPhyDatRen=splitPhyDat.rename(columns={splitPhyDat.columns[6]: 'Gtdb_taxa'})
    expTax=splitPhyDatRen[['Gtdb_taxa']]
    expTax['Gtdb_taxa']=expTax['Gtdb_taxa'].str.replace('s__', '')
    expTax['Gtdb_taxa']=expTax['Gtdb_taxa'].str.replace('Clostridium difficile', 'Clostridioides difficile')
    gtdbTax=pd.concat([df[['user_genome']], expTax], axis=1)
    gtdbTax = gtdbTax.rename(columns={'user_genome': 'uuid'})
    return gtdbTax

# get species names from original metadata
def getMetadatSpec(metadat):
    metadatSpec=metadat[['uuid', 'Organism']]
    metadatSpec=metadatSpec.rename(columns={'Organism':'Original_taxa'})
    metadatSpec['Original_taxa']=metadatSpec['Original_taxa'].str.replace('Clostridium difficile', 'Clostridioides difficile')
    return metadatSpec

# merge gtdbtk and original data
def mergeDat():
    df1=getGtdbSpec(df)
    df2=getMetadatSpec(metadat)
    mergedDat=pd.merge(df1, df2, left_on='uuid', right_on='uuid', how='left')
    return mergedDat

def findMatched():
    df=mergeDat()
    matched=df.loc[df['Gtdb_taxa']==df['Original_taxa']]
    return matched

def findMismatch():
    df=mergeDat()
    mismatched=df.loc[df['Gtdb_taxa']!=df['Original_taxa']]
    return mismatched






