from sklearn.datasets import make_classification
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV
import joblib
from distributed import Client
import socket
import time

start_time = time.time()

output_path = "model.pkl"

client = Client(f"tcp://{socket.gethostbyname(socket.gethostname())}:8786")

X, y = make_classification(n_samples=1000, random_state=0)

param_grid = {
    "C": [0.001, 0.01, 0.1, 0.5, 1.0, 2.0, 5.0, 10.0],
    "kernel": ["rbf", "poly", "sigmoid"],
    "shrinking": [True, False],
}


grid_search = GridSearchCV(
    SVC(gamma="auto", random_state=0, probability=True),
    param_grid=param_grid,
    return_train_score=False,
    cv=3,
    n_jobs=-1,
)

with joblib.parallel_backend("dask"):
    grid_search.fit(X, y)

joblib.dump(grid_search, output_path)


client.shutdown()
client.close()
print("--- %s seconds ---" % (time.time() - start_time))
