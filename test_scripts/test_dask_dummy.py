from time import sleep
from dask import delayed
from distributed import Client
import dask

print('connecting')

client = Client("127.0.0.1:8786")

print("connected")

def double(x):
    sleep(1)
    return 2 * x


def is_even(x):
    return not x % 2


def inc(x):
    sleep(1)
    return x + 1

def main():
    data = [12, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    results = []
    for x in data:
        if is_even(x):  
            y = delayed(double)(x)
        else:  
            y = delayed(inc)(x)
        results.append(y)

    total = delayed(sum)(results)
    return total.compute()

print('done')