import pandas as pd

#Leitura do csv e remocao da coluna 'genre'
df = pd.read_csv('goodreads_books.csv')

nRows = len(df.index)
nNans = [df[col].isna().sum() for col in df]

print(f"Num. linhas: {nRows}")
for col,n in zip(df,nNans):
    print(f"NaN {col}: {n}")