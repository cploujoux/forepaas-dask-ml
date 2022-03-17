from distributed import Client
from time import sleep
from dask import delayed
import socket
import time

print(socket.gethostbyname(socket.gethostname()))


print("connecting")
client = Client(f"tcp://{socket.gethostbyname(socket.gethostname())}:8786")
print("connected")

# print("connecting")
# df = dd.read_sql_table(
#     table="consommations",
#     uri="postgresql+psycopg2://root:password@127.0.0.1:5432/test",
#     index_col="conso_id",
# )
# print("connected")


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
    for x in range(10):
        if is_even(x):
            y = delayed(double)(x)
        else:
            y = delayed(inc)(x)
        results.append(y)

    total = delayed(sum)(results)
    print("graph computed")
    return total.compute()


if __name__ == "__main__":
    print("hi")
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
    # print("Done")
    f = open("output.txt", "w")
    f.write("Hello I am the result from the job the real one one one one")
    f.close()
    client.shutdown()
    client.close()
