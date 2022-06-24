import pandas as pd

df=pd.read_csv("data/gtdbtk.bac120.summary.tsv",sep='\t', converters={'user_genome': lambda x: str(x)})

for i in df.columns:
    print(i)