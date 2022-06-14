
import pandas as pd
df=pd.read_csv("/home/ubuntu/ICMC/demoMultSpecies/gtdbtk/output/classify/gtdbtk.bac120.summary.tsv",sep='\t')
# select column
df_1=df.iloc[:, [1]]
# split column based on pattern
df_2=df_1['classification'].str.split(';', expand=True)

df_3=df_2.iloc[:, [6]]
# rename column
df_4= df_3.rename(columns={df_3.columns[0]: 'Experiment_Taxa'})
# replace part of the string in the column
df_4['Experiment_Taxa'] = df_4['Experiment_Taxa'].str.replace('s__', '')

#df_5=pd.DataFrame(df_4.Experiment_Taxa.replace({'s__':''}, regex=True))




for variable in dir():
    if variable[0:2] != "__":

        del globals()[variable]
 
    
        
