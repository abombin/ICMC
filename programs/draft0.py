import pandas as pd

gtdbDat=pd.read_csv('C:\Users\abomb\OneDrive - Emory University\bacteria\data\gtdb\ar53_metadata_r207.tsv', sep='\t')

print(gtdbDat.columns)