import dask
import dask.dataframe as dd
from sqlalchemy import sql

print('connecting')
df = dd.read_sql_table("consommations","postgresql+psycopg2://root:password@127.0.0.1:5432/test", index_col = 'conso_id');
print('connected')
print(df)
