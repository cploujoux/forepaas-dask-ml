import dask.dataframe as dd
from time import sleep
from dask import delayed
from distributed import Client


client = Client("tcp://127.0.0.1:8786")
df = dd.read_sql_table("consommations","postgresql+psycopg2://root:password@127.0.0.1:5432/test", index_col = 'conso_id')

print(df)

def double(x):
    sleep(1)
    return 2 * x


def is_even(x):
    return not x % 2


def inc(x):
    sleep(1)
    return x + 1

def main():
    results = []
    for _ in range(10000):
        df.groupby("lat").max()
        # for x in df.loc['lat']:
            # if is_even(x):
            #     y = delayed(double)(x)
            # else:  
            #     y = delayed(inc)(x)
            # results.append(y)

    total = delayed(sum)(results)
    print("graph computed")
    return total.compute()


if __name__ == "__main__":
    main()
    print('Done')
