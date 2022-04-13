from dask.distributed import Client
from dask_ml.naive_bayes import GaussianNB
from dask_ml.datasets import make_classification
import socket
import joblib
import time
import sys


if __name__ == "__main__":
    start_time = time.time()
    sys.stdout.flush()

    client = Client(f"tcp://{socket.gethostbyname(socket.gethostname())}:8786")
    # client = Client()
    print("connected")
    print("--- %s seconds ---" % (time.time() - start_time))

    X, y = make_classification(n_samples=7000, chunks=50, n_features=5, random_state=0)

    print("created dataset")
    print("--- %s seconds ---" % (time.time() - start_time))
    gnb = GaussianNB()

    print("starting fit")
    print("--- %s seconds ---" % (time.time() - start_time))
    gnb.fit(X, y)
    print("fit ended")
    print("--- %s seconds ---" % (time.time() - start_time))

    output_path = "model.pkl"
    joblib.dump(gnb, output_path)

    client.shutdown()
    client.close()
    print("--- %s seconds ---" % (time.time() - start_time))
