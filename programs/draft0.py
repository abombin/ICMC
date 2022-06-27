import pandas as pd

d = {'col1': [1, 2], 'col2': [3, 4]}
df = pd.DataFrame(data=d)

column_names = ["col1", "col2"]

df1 = pd.DataFrame(columns=['col1', 'col2'])


df3 = pd.DataFrame(data=d)



df2=pd.concat([df1,df, df3], ignore_index=True).reset_index()

print(df2)