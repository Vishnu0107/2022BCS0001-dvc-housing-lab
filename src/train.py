import pandas as pd
import pandas as pd
df = pd.read_csv("data/housing.csv")
print(df.shape)
df = pd.read_csv("data/housing.csv")
df_small = df.head(5000)
df_small.to_csv("data/housing.csv", index=False)
print("Rows:", df_small.shape[0])