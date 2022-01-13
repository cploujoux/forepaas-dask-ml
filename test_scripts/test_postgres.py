import dask.dataframe as dd
from distributed import Client

print('connecting')
client = Client("tcp://127.0.0.1:8786")
print("connected")

print("connecting")
df = dd.read_sql_table(
    table="consommations",
    uri="postgresql+psycopg2://root:password@127.0.0.1:5432/test",
    index_col="conso_id",
)
print("connected")
print(df)
