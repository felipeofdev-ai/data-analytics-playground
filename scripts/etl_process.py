import pandas as pd
from sqlalchemy import create_engine

# Carregar dados
df = pd.read_csv("../data/sample_data.csv")

# Transformações simples
df["salary_k"] = df["salary"] / 1000
df["senior"] = df["age"].apply(lambda x: x > 30)

# Conectar ao banco SQLite
engine = create_engine("sqlite:///../data/data.db", echo=True)
df.to_sql("employees", con=engine, if_exists="replace", index=False)

print("ETL completed! Data inserted into SQLite database.")
