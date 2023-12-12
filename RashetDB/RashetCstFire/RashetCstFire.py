import pandas as pd

df = pd.read_csv("test.csv")[:100]
df1 = df['a']
print(df1)
