import numpy as np
from dask.distributed import Client
import joblib
from sklearn.datasets import load_digits
from sklearn.model_selection import RandomizedSearchCV
from sklearn.svm import SVC
import socket
import time

# is subject to the bug https://github.com/joblib/joblib/issues/1201


if __name__ == "__main__":
    start_time = time.time()

    output_path = "model.pkl"

    client = Client(f"tcp://{socket.gethostbyname(socket.gethostname())}:8786")
    # client = Client()

    digits = load_digits()

    param_space = {
        "C": np.logspace(-6, 6, 13),
        "gamma": np.logspace(-8, 8, 17),
        "tol": np.logspace(-4, -1, 4),
        "class_weight": [None, "balanced"],
    }

    model = SVC(kernel="rbf")
    search = RandomizedSearchCV(model, param_space, cv=3, n_iter=50, verbose=10)

    with joblib.parallel_backend("dask"):
        search.fit(digits.data, digits.target)

    joblib.dump(search, output_path)

    client.shutdown()
    client.close()
    print("--- %s seconds ---" % (time.time() - start_time))
