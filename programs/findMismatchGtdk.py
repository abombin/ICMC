
import pandas as pd
# gtdb summary
df=pd.read_csv("data/gtdbtk.bac120.summary.tsv",sep='\t', converters={'user_genome': lambda x: str(x)})
# original metadata
metadat=pd.read_csv("data/metaDat.csv", converters={'uuid': lambda x: str(x)})
# gtdb NCBI dictionary
gtdbDat=pd.read_csv('C:/Users/abomb/OneDrive - Emory University/bacteria/data/gtdb/gtdbtkNcbiDict.tsv', sep='\t')
   
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

# get samples that match metadata
def findMatched():
    df=mergeDat()
    matched=df.loc[df['Gtdb_taxa']==df['Original_taxa']]
    return matched

# get samples that mismatch metadata
def findMismatch():
    df=mergeDat()
    mismatched=df.loc[df['Gtdb_taxa']!=df['Original_taxa']]
    return mismatched

# check if mismatch was due to misspelling
def checkDictionary():
    df=findMismatch()
    df['Ncbi_match']=''
    for i in range(0, len(df.index)):
        taxa=df['Gtdb_taxa'][i]
        dfMatch=gtdbDat[gtdbDat['gtdb_taxonomy'].str.contains(taxa)].reset_index()
        if df['Original_taxa'][i]==dfMatch['ncbi_organism_name'][0]:
            df['Ncbi_match'][i]=dfMatch['ncbi_organism_name'][0]
        else:
            df['Ncbi_match'][i]=='No_match'
    return df

print(checkDictionary())







